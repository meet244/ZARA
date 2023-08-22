import customtkinter
from PIL import Image
import markdown2
import re

def markdown_to_text(markdown_content):
    html_content = markdown2.markdown(markdown_content)
    text_content = re.sub('<[^<]+?>', '', html_content)
    return text_content

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x600")

def enterPress(btn):
    if(entry.get()==""):
        button_listen()
    else:button_send()
app.bind('<Return>', enterPress)

app.grid_columnconfigure((0,2), weight=0)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure((0, 2), weight=0)
# todo change image paths
send_image = customtkinter.CTkImage(dark_image=Image.open("send-dark.png"),size=(25,25))
mic_image = customtkinter.CTkImage(dark_image=Image.open("mic-dark.png"),size=(25,25))

def format_text(text, max_width=27):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) <= max_width:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    formatted_text = "\n".join(lines)
    num_lines = len(lines)
    
    return formatted_text, num_lines

def button_listen():
    print("button listen")
listen_btn = customtkinter.CTkButton(app, text="", fg_color="transparent",width=30, height=30, command=button_listen, image=mic_image)
listen_btn.grid(row=2,column=0,padx=(5,5),pady=(10,10))

entry = customtkinter.CTkEntry(app, placeholder_text="Ask Anything...")
entry.grid(row=2 ,column=1,pady=(10,10),sticky="nsew")

def button_send():
    tex,c = format_text(entry.get())
    textbox = customtkinter.CTkTextbox(scrollable_frame,activate_scrollbars=False, height=25*c if(c<=20) else 20,width=300)
    textbox.insert('0.0',tex)
    textbox.configure(state="disabled", wrap="word")  # configure textbox to be read-only
    textbox.grid(row=len(allMessage)+1,column=0, padx=(5,5), pady=(5,5), sticky="ne")
    allMessage.append(textbox)
    print("button send")
send_btn = customtkinter.CTkButton(app, text="", fg_color="transparent",width=30, height=30, command=button_send, image=send_image)
send_btn.grid(row=2,column=2,padx=(5,5),pady=(10,10))

scrollable_frame = customtkinter.CTkScrollableFrame(app,width=450,height=300,label_anchor='s')
scrollable_frame.grid(column=0,row=1,sticky="nsew",columnspan=3)
scrollable_frame.grid_columnconfigure(0,weight=1)
scrollable_frame.grid_rowconfigure(0,weight=1)

allMessage = []

def user_say(thing):
    tex,c = format_text(thing)
    textbox = customtkinter.CTkTextbox(scrollable_frame,activate_scrollbars=False, height=25*c if(c<=20) else 20,width=300)
    textbox.insert('0.0',tex)
    textbox.configure(state="disabled", wrap="word")  # configure textbox to be read-only
    textbox.grid(row=len(allMessage)+1,column=0, padx=(5,5), pady=(5,5), sticky="ne")
    allMessage.append(textbox)

def zara_say(thing):
    tex,c = format_text(thing)
    textbox = customtkinter.CTkTextbox(scrollable_frame,activate_scrollbars=False, height=25*c if(c<=20) else 20,width=300, fg_color="#165182")
    textbox.insert('0.0',tex)
    textbox.configure(state="disabled", wrap="word")  # configure textbox to be read-only
    textbox.grid(row=len(allMessage)+1,column=0, padx=(5,5), pady=(5,5), sticky="nw")
    allMessage.append(textbox)



user_say("hi")

zara_say("hello how can i help?")


app.mainloop()

print("hiii")