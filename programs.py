import requests
import wolframalpha
import json
import time
import re
import os
import subprocess
import wikipedia
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()
import os

def startProgramLocal(name):

  useless = ["launch","start","open","please","and"]
  for u in useless:
      name = name.replace(u,"")
  name = name.strip()
  print(name)

  directory_path1 = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
  directory_path2 = os.path.expanduser("~")+r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"

  def list_shortcuts(directory):
      shortcuts = []

      for root, dirs, files in os.walk(directory):
          for file in files:
              if file.lower().endswith('.lnk'):
                  shortcuts.append(os.path.join(root, file))

      return shortcuts

  shortcuts_list = list(list_shortcuts(directory_path1) + list_shortcuts(directory_path2))
  finals = []
  for app in name.split(" "):
    app = app.strip()
    if(app==""):continue
    for shortcut in shortcuts_list:
        if(app.lower() in shortcut.split("\\")[-1].replace(".lnk","").lower()):
            finals.append(shortcut)
  print(finals)
  
  if(len(finals)>1):
      if(len(finals)<5):
        for f in finals:
          subprocess.Popen([f], shell=True)
        return True
      else:
         return False

  elif(len(finals)==1):
      subprocess.Popen([finals[0]], shell=True)
      return True
  else:
      return False
      # print("No apps found to launch")

def set_alarm(sentence: str):
  # time = get_alarm_time(sentence)
  time_pattern = r'(\d{1,2}):?(\d{2})?\s?(AM|PM)?'
  match = re.search(time_pattern, sentence, re.IGNORECASE)
  now = datetime.now()
  plus_day = False

  if match:
    hours = int(match.group(1))
    minutes = int(match.group(2) or 0)
    am_pm = match.group(3)

    if am_pm:
      if am_pm.lower() == 'pm':
        hours += 12
    else:
      # Extract the hour from the current time
      if (hours > 12):
        current_hour = datetime.now().time().hour
      else:
        current_hour = int(datetime.now().time().strftime('%H'))

      current_min = datetime.now().time().minute
      if hours < current_hour or (hours == current_hour
                                  and minutes <= current_min):
        # now += timedelta(days=1)  # Set alarm for the same time on the next day
        if (hours <= 12): hours += 12
        else: plus_day = True

    time = hours, minutes

    if time:

      hours, minutes = time

      # now = datetime.now()
      alarm_time = now.replace(hour=hours,
                               minute=minutes,
                               second=0,
                               microsecond=0)
      if plus_day:
        alarm_time += timedelta(
            days=1
        )  # Set alarm for tomorrow if the time has already passed today

      if alarm_time <= now:
        alarm_time += timedelta(
            days=1
        )  # Set alarm for tomorrow if the time has already passed today

      time_difference = alarm_time - now
      alarm_milliseconds = time_difference.total_seconds() * 1000

      alarm_milliseconds = int(alarm_time.timestamp())

      # print(f"Alarm Time: {hours:02d}:{minutes:02d}")
      # print(f"Alarm Milliseconds: {alarm_milliseconds} ms")
      # print()

      timer_data = {}
      data = []
      with open('time.json', 'r') as file:
        data = json.load(file)

      data.append({alarm_milliseconds: 'alarm'})

      with open('time.json', 'w') as file:
        json.dump(data, file)

      # print("Alarm saved to 'time.json'.")
    else:
      print(f"No valid time found in sentence: {sentence}\n")

def convert_to_seconds(value, unit):
    if unit.startswith('minute') or unit.startswith('min'):
        return value * 60
    elif unit.startswith('second') or unit.startswith('sec'):
        return value
    elif unit.startswith('hour') or unit.startswith('hr'):
        return value * 3600
    elif unit.startswith('day'):
        return value * 86400
    else:
        raise ValueError(f"Invalid unit: {unit}")
def timer(sentence):
  regex_pattern = r"(\d+)\s*(minutes?|mins?|seconds?|secs?|hours?|hrs?|days?)\s*((?:and|,)?\s*(\d+)\s*(minutes?|mins?|seconds?|secs?|hours?|hrs?|days?))?(\s*from now)?"

  matches = re.findall(regex_pattern, sentence, re.IGNORECASE)
  total_seconds = 0
  for match in matches:
    value1 = int(match[0])
    unit1 = match[1]
    value2 = int(match[3]) if match[3] else None
    unit2 = match[4] if match[4] else None
    from_now = bool(match[5])

    total_seconds += convert_to_seconds(value1, unit1)
    if value2 and unit2:
      total_seconds += convert_to_seconds(value2, unit2)
    if from_now:
      pass

  timer_data = {}

  current_time = int(time.time())
  timer_time = current_time + total_seconds

  timer_data[timer_time] = "timer"

  with open('time.json', 'r') as file:
    data = json.load(file)

  data.append(timer_data)

  with open('time.json', 'w') as file:
    json.dump(data, file)

  # print("Timer saved to 'time.json'.")

def wolfarm(query):
  try:
    requester = wolframalpha.Client(os.getenv("WOLFARM_API"))
    requested = requester.query(query)
    try:
      Answer = next(requested.results).text
      if("data not provided" in Answer):raise Exception()
      return str(Answer)
    except:
      return("An String Value Is Not Answerable.")
  except:
    return("Invalid Wolframalpha API key")

def temp(query):
  query = query.replace('what is ', '').replace('tell me about ','').replace('tell me ', '')
  url = 'https://www.google.com/search?q=' + query
  headers = {
      'User-Agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
  }
  r = requests.get(url, headers=headers)
  data = BeautifulSoup(r.text, 'html.parser')
  temp = data.find('div', class_='BNeawe').text
  air = (data.find('div', class_='tAd8D').text).split('\n')
  return f"{query} is {temp} and {air[1]}"

def travel(query):
  url = f"https://www.google.com/search?q={query}"
  
  response = requests.get(url)
  
  soup = BeautifulSoup(response.content, "html.parser")
  
  search_results = soup.find("div", class_="BNeawe")
  
  if search_results:
      # Extract and print the route and duration
      route_and_duration = search_results.get_text()
      return route_and_duration
  else:
      return "No information found."

def get_wikipedia_summary(query):
  try:
    summary = wikipedia.summary(query, sentences=2)
    return summary
  except Exception:
    return "Sorry, no answer."

def convert(query):
  query = query.replace('what is ', '').replace('tell me about ','').replace('tell me ', '')
  url = 'https://www.google.com/search?q=' + query
  headers = {
      'User-Agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
  }
  r = requests.get(url, headers=headers)
  data = BeautifulSoup(r.text, 'html.parser')
  temp = data.find('div', class_='BNeawe').text
  return f"{temp}"

def print_news(keyword="india"):
    base_url = "https://newsapi.org/v2/everything"
    
    params = {
        "apiKey": os.getenv("NEWSAPI_KEY"),
        "q": keyword,
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        
        if articles:
            ret = ''
            for idx, article in enumerate(articles, start=1):
                title = article.get("title", "No title available")
                source = article.get("source", {}).get("name", "Unknown source")
                description = article.get("description", "No description available")
                
                ret += (f"Article: {idx}\n")
                ret += (f"Title: {title}\n")
                ret += (f"Source: {source}\n")
                ret += (f"Description: {description}\n\n")
            return ret
        else:
            return("No articles found.")
    else:
        return("Error fetching news data.")