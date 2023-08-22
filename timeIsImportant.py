import json
import time
import pygame

def load_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def schedule_alarms_and_timers(data):
    for item in data:
        timestamp, event = int(list(item.keys())[0]), list(item.values())[0]
        current_time = time.time()
        
        if timestamp <= current_time:
            print(f"Skipping {event} at {timestamp} as it's in the past.")
            continue
        
        wait_time = timestamp - current_time
        print(f"Scheduling {event} at {timestamp} ({wait_time:.2f} seconds from now).")
        
        time.sleep(wait_time)
        
        if event == "alarm":
            play_sound("wake.mp3")
        elif event == "timer":
            play_sound("wake.mp3")

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
    data = load_json("time.json")
    schedule_alarms_and_timers(data)
