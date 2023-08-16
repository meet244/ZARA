import programs
import openAssist
import flans
import re
import pywhatkit as kit
import pyautogui as pg

def ZARA(query):
    # query = "open chrome"
    # query = "make a simple hi program in java"
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

    for w in resp1.split(" "):
        if(w in ["start","open","launch","software"]):
            # fun
            programs.startProgramLocal(query)
            return("launching it")
        if(w in ["code"]):
            # oa
            resp = openAssist.response(query)
            if("write" in query or "paste" in query):
                if('```' in resp):
                    pattern = r'```(.*?)```'
                    # Find all matches using the re.findall() function
                    matches = re.findall(pattern, resp, re.DOTALL)  # re.DOTALL matches across newlines

                    # Print each match (i.e., the extracted code blocks)
                    for match in matches:
                        pg.write(match.strip())
                        pg.write("/n")
                else:
                    pg.write(resp)
            return(resp)
        if(w in ["math"]):
            # flan oa
            print("wolfarm")
            print(programs.wolfarm(query))
            print("Flan")
            return(flans.response(query))
        if(w in ["gk"]):
            # oa
            print("oA")
            return(openAssist.response(query))
            print("wolfarm")
            return(programs.wolfarm(query))
        if(w in ["conversion","unit"]):
            return(programs.convert(query))
            break
        if(w in ["alarm"]):
            # fun
            programs.set_alarm(query)
            return("alaram set")
        if(w in ["timer"]):
            # fun
            programs.timer(query)
            return("timer set")
        if(w in ["song","music"]):
            # fun  
            words = ['play','song','music']
            for w in words:
                query = query.replace(w,"")
            kit.playonyt(query)
            return ("playing it")
        if(w in ["weather"]):
            # fun
            return(programs.temp(query))
        if(w in ["news"]):
            # fun
            return("a news line")
        if(w in ["navigation"]):
            # fun
            return(programs.travel(query))
        if(w in ["others","other"]):
            # oa
            return(openAssist.response(query))