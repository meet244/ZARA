import final
import pvporcupine
import pyaudio
import struct
import playsound
import pygame
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import re

porcupine = pvporcupine.create(keyword_paths=["Hey-Zara_en_windows_v2_1_0.ppn"],access_key="gltlepsfo/R5vPk3AH/JQQXYSD0urATF/ILqfeQDpjdCWq6/ZTR8RA==")

pa = pyaudio.PyAudio()
pygame.init()

# Set the frequency and size of the audio
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

# Load the sound file
sound_file = 'wake.mp3'
sound = pygame.mixer.Sound(sound_file)

audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length)

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
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return None
    return query

if __name__ == "__main__":
    try:
        print("READY")
        while(1):
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack("h"*porcupine.frame_length,keyword)
            keyword_index = porcupine.process(keyword)
            if keyword_index>=0:
                print('done')
                # playsound.playsound(r'C:\Users\meet2\Downloads\Chat-App-OpenAssistant-API-main\Chat-App-OpenAssistant-API-main\wake.mp3', True)
                sound.play()
                # playsound.playsound('C:\\Users\\meet2\\Downloads\\Chat-App-OpenAssistant-API-main\\Chat-App-OpenAssistant-API-main\\wake.mp3', True)
                query = takeCommand()
                if query:
                    query = query.lower()
                    speak(final.ZARA(query))
                # song = pydub.AudioSegment.from_mp3('C:\\Users\\meet2\\Desktop\\zara\\wake.mp3')
                # pydub.playback.play(song)


    finally:
        porcupine.delete()
        audio_stream.close()
    