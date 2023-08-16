import final
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)
engine.setProperty('rate', 160)


def speak(audio):
    if audio:
        print(audio)
        engine.say(audio)
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
    
    while True:
        query = takeCommand().lower()
        if query:
            speak(final.ZARA(query))





