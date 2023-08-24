import programs
import openAssist
import flans
import re
import pywhatkit as kit
import pyautogui as pg

def ZARA(query):
    print("Understanding")
    # query = "open chrome"
    # query = "make a simple hi program in java"
    # There is a basket containing 5 apples, how do you divide the apples among 5 children so that each child has 1 apple while 1 apple remains in the basket?
    # query = "Ariel was playing basketball. 1 of her shots went in the hoop. 2 of her shots did not go in the hoop. How many shots were there in total?"
    # query = "which is tallest building in world?"
    # query = "set alarm at 5 pm."
    # query = "make timer for 1 minute"
    # query = "play aaisa dekha nahi khubsoorat koi"
    # query = "current temperature at new york"
    # query = "take from mumbai to goa"
    # query = "what is your name?"


    if(query.strip() == ""):return

    resp1 = flans.classify(query)
    
    print("Thinking")
    for w in resp1.split(" "):
        if(w in ["start","open","launch","software"]):
            if programs.startProgramLocal(query):
                return("Launching it")
            else:
                return("Still learning to do so")
        if(w in ["code"]):
            resp = openAssist.response(query)
            if("write" in query or "paste" in query):
                if('```' in resp):
                    pattern = r'```(.*?)```'
                    matches = re.findall(pattern, resp, re.DOTALL)
                    for match in matches:
                        tex = match.strip()
                        pg.write(tex)
                else:
                    pg.write(resp)
            return(resp)
        if(w in ["math"]):
            return(flans.Mathresponse(query))
        if(w in ["gk"]):
            return(programs.wolfarm(query))
        if(w in ["conversion","unit"]):
            return(programs.convert(query))
        if(w in ["alarm"]):
            programs.set_alarm(query)
            return("Alaram set")
        if(w in ["timer"]):
            programs.timer(query)
            return("Timer set")
        if(w in ["song","music"]):
            words = ['play','song','music']
            for w in words:
                query = query.replace(w,"")
            kit.playonyt(query)
            return ("Playing it")
        if(w in ["weather"]):
            return(programs.temp(query))
        if(w in ["news"]):
            return(programs.print_news(query))
        if(w in ["navigation"]):
            return(programs.travel(query))
        if(w in ["wikipedia"]):
            return(programs.get_wikipedia_summary(query))
        if(w in ["others","other","conversation"]):
            return(openAssist.response(query))