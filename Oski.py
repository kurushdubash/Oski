import speech_recognition as sr
import requests
from datetime import datetime


def get_audio():
    r = sr.Recognizer(language = "en-US", key = "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
    r.energy_threshold = 1200
    r.pause_threshold = 0.5
    with sr.Microphone() as source:                # use the default microphone as the audio source
         print("Listening...")
         audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    try:
        print("Transcribing..")
        transcribed_audio = r.recognize(audio)   # recognize speech using Google Speech Recognition
        return transcribed_audio
    except LookupError:                            
        print("Could not understand audio") # speech is unintelligible 
        print("Trying again.")
        return get_audio()

def get_football_info(audio):
    football_api_url = 'http://api.sportsdatallc.org/ncaafb-t1/2014/REG/schedule.json?api_key=6r45ruu32nbydywtds97krap'
    football_data = requests.get(football_api_url)
    football_dict = football_data.json()
    return football_dict

def gym_info(audio):
    if 'hours' in audio or 'close' in audio or 'does open':
        print('Sun: 8am - 1am')
        print('Mon: 6am - 1am')
        print('Tue: 6am - 1am')
        print('Wed: 6am - 1am')
        print('Thu: 6am - 1am')
        print('Fri: 6am - 11pm')
        print('Sat: 8am - 11pm')

    if 'open' in audio or 'closed' in audio:
        time_info = datetime.today()
        time = str(datetime.now().time())
        day_of_week = time_info.weekday()
        hours = ''
        for char in time:
            if(char != ':'):
                hours = hours + char
            else:
                break

        hours = int(hours)
        if(day_of_week < 6 and hours >= 6):
            if(day_of_week == 4 and hours > 23):
                print("Gym closed!")
            else:
                print("Gym open!")
        elif(day_of_week > 4 and hours >= 8):
            if(day_of_week == 5 and hours > 23):
                print("Gym closed!")
            else:
                print("Gym open!")
        else:
            print("Gym closed")

def parse_audio(audio):
    if 'football' in audio:
        print("true")
        print(get_football_info(audio))
    if 'rsf' in audio or 'gym' in audio:
        gym_info(audio)

def run():
    transcribed_audio = get_audio().lower()
    print(transcribed_audio)
    parse_audio(transcribed_audio)
    return transcribed_audio




