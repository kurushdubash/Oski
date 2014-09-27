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
        return 'poop'

def get_football_info(audio):
    football_api_url = 'http://api.sportsdatallc.org/ncaafb-t1/2014/REG/schedule.json?api_key=6r45ruu32nbydywtds97krap'
    football_data = requests.get(football_api_url)
    football_dict = football_data.json()
    return football_dict

def gym_info(audio):
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
        # print('hours:', hours)
        # print('day of week', day_of_week)

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

        # print(time)
        # print(time_info.weekday())


def parse_audio(audio):
    if 'football' in audio:
        print("true")
        print(get_football_info(audio))
    if 'rsf' in audio or 'gym' in audio:
        gym_info(audio)


transcribed_audio = get_audio()
print(transcribed_audio.capitalize())
parse_audio(transcribed_audio)





