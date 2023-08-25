import final
import pvporcupine
import pyaudio
import struct
from tkinter import PhotoImage
import pygame
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import re
import customtkinter
from PIL import Image, ImageTk
import markdown2
import threading
import timeIsImportant
from dotenv import load_dotenv
load_dotenv()
import os

# VARS
colorDB = "#165182"
colorDB = "#4286F5"

# LOADING GUI

def markdown_to_text(markdown_content):
    html_content = markdown2.markdown(markdown_content)
    text_content = re.sub('<[^<]+?>', '', html_content)
    return text_content
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("ZARA")
app.geometry("400x600")
app.iconbitmap("zara.ico")

def enterPress(btn):
    if(entry.get()==""):
        button_listen()
    else:button_send()
app.bind('<Return>', enterPress)

app.grid_columnconfigure((0,2), weight=0)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure((0, 2), weight=0)

send_image = customtkinter.CTkImage(dark_image=Image.open("send.png"),size=(25,25))
mic_image = customtkinter.CTkImage(dark_image=Image.open("mic-dark.png"),size=(25,25))

def button_listen():
    # print("button listen")
    takeCommand()
listen_btn = customtkinter.CTkButton(app, text="",bg_color="transparent", fg_color="transparent",width=30, height=30, command=button_listen, image=mic_image)
listen_btn.grid(row=2,column=0,padx=(5,5),pady=(10,10))

entry = customtkinter.CTkEntry(app, placeholder_text="Ask Anything...")
entry.grid(row=2 ,column=1,pady=(10,10),sticky="nsew")

def button_send():
    if(str(entry.get()).strip()!=""):
        user_say(str(entry.get()).strip())
        # print("button send")
        t = threading.Thread(target=askZARA)
        t.start()

send_btn = customtkinter.CTkButton(app, text="",bg_color="transparent", fg_color="transparent",width=30, height=30, command=button_send, image=send_image)
send_btn.grid(row=2,column=2,padx=(5,5),pady=(10,10))

scrollable_frame = customtkinter.CTkScrollableFrame(app,width=450,height=300,label_anchor='s')
scrollable_frame.grid(column=0,row=1,sticky="nsew",columnspan=3)
scrollable_frame.grid_columnconfigure(0,weight=1)
scrollable_frame.grid_rowconfigure(0,weight=1)

allMessage = []

def user_say(thing):
    textbox = customtkinter.CTkTextbox(scrollable_frame, height=500,width=300)
    textbox.insert('0.0',thing)
    textbox.configure(state="disabled", wrap="word")  # configure textbox to be read-only
    last_line = textbox.index("end-1c").split(".")[0]
    wordPerLine = 0
    for l in (thing.split("\n")):
        wordPerLine += int(len(l.split(" "))/8)
    textbox.configure(height=(20*(int(last_line)+wordPerLine)))
    textbox.grid(row=len(allMessage)+1,column=0, padx=(5,5), pady=(5,5), sticky="ne")
    allMessage.append(textbox)

def zara_say(thing):
    try:
        textbox = customtkinter.CTkTextbox(scrollable_frame, height=500,width=300, fg_color=colorDB)
        textbox.insert('0.0',thing)
        textbox.configure(state="disabled", wrap="word")  # configure textbox to be read-only
        last_line = textbox.index("end-1c").split(".")[0]
        wordPerLine = 0
        for l in (thing.split("\n")):
            wordPerLine += int(len(l.split(" "))/8)
        textbox.configure(height=(20*(int(last_line)+wordPerLine)))
        textbox.grid(row=len(allMessage)+1,column=0, padx=(5,5), pady=(5,5), sticky="nw")
        allMessage.append(textbox)
        t = threading.Thread(target=speak,args=(thing,))
        t.isDaemon = True
        t.start()
    except:pass


#LOADING ZARA

def askZARA():
    if(entry.get() == ""):return
    resp = final.ZARA(entry.get())
    if(resp.strip()==""):return
    entry.delete(0,"end")
    # print(resp)
    zara_say(resp.replace('```',"\n\n"))

porcupine=None
try:
    porcupine = pvporcupine.create(keyword_paths=["Hey-Zara_en_windows_v2_1_0.ppn"],access_key=os.getenv("PORCUPINE_API"))
except Exception:pass

pa = pyaudio.PyAudio()
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
sound_file = 'wake.mp3'
sound = pygame.mixer.Sound(sound_file)

audio_stream = None
try:
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)
except Exception as e:
    pass

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)
engine.setProperty('rate', 160)

def speak(audio):
    if audio:
        print(audio)
        pattern = r"```.*?```"
        cleaned = re.sub(pattern, "", audio, flags=re.DOTALL)
        engine.say(cleaned)
        engine.runAndWait()

def takeCommand():
    if(not audio_stream):return
    r = sr.Recognizer()
    prev_color = listen_btn.cget("fg_color")
    query = None
    with sr.Microphone() as source:
        print("Listening...")
        listen_btn.configure(fg_color=colorDB)
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Recognizing...")
        listen_btn.configure(fg_color=prev_color)
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")

    if(query):
        entry.insert(0,query)

def waitWakeUp():
    try:
        print("Speak Up")
        while(1):
            if(not audio_stream):return
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack("h"*porcupine.frame_length,keyword)
            keyword_index = porcupine.process(keyword)
            if keyword_index>=0:
                sound.play()
                takeCommand()
    finally:
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()

if __name__ == "__main__":
    wake = threading.Thread(target=timeIsImportant.start)
    wake.daemon = True
    wake.start()
    wake = threading.Thread(target=waitWakeUp)
    wake.daemon = True
    wake.start()
    zara_say("Say 'Hey Zara' or use UI to have a chit-chat..")
    zara_say("Hello, how can I help?")
    app.mainloop()