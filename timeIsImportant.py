import json
import time
import pygame
import os

def load_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def schedule_alarms_and_timers(data):
    current_time = time.time()
    updated_data = []
    
    for item in data:
        timestamp, event = int(list(item.keys())[0]), list(item.values())[0]
        
        if timestamp <= current_time:
            # print(f"Skipping {event} at {timestamp} as it's in the past.")
            continue
        
        wait_time = timestamp - current_time
        # print(f"Scheduling {event} at {timestamp} ({wait_time:.2f} seconds from now).")
        
        time.sleep(wait_time)
        
        if event == "alarm":
            play_sound("wake.mp3")
        elif event == "timer":
            play_sound("wake.mp3")
        
        current_time = time.time()
        updated_data.append(item)
    
    return updated_data

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def create_json(filename):
    with open(filename, 'w') as file:
        json.dump([], file)

def start():
    if not os.path.exists("time.json"):
        create_json("time.json")
    while True:
        data = load_json("time.json")
        updated_data = schedule_alarms_and_timers(data)
        
        with open("time.json", "w") as file:
            json.dump(updated_data, file, indent=4)
        
        time.sleep(30)  # Wait for 30 seconds before the next iteration
