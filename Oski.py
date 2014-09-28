import speech_recognition as sr
import requests
from datetime import datetime


def get_audio():
    r = sr.Recognizer(language = "en-US", key = "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
    r.energy_threshold = 1800
    r.pause_threshold = 0.5
    with sr.Microphone() as source:                # use the default microphone as the audio source
         print("Listening...")
         audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    try:
        print("Transcribing..")
        transcribed_audio = r.recognize(audio)   # recognize speech using Google Speech Recognition
        if(transcribed_audio == ''):
            print("Could not understand audio") # speech is unintelligible 
            print("Trying again.")
            return get_audio()
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
    if 'hours' in audio or ('when' in audio and 'close' in audio):
        return get_gym_schedule()

    if 'open' in audio or 'closed' in audio or 'close' in audio:
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
        result = gym_open_or_closed(hours, day_of_week)
        
        result_text = " Open" if result else " Closed"
        return "The Gym is" + result_text

def get_gym_schedule():
	return 'Sun: 8am - 1am\n' + 'Mon: 6am - 1am\n' + 'Tue: 6am - 1am\n' + 'Wed: 6am - 1am\n' + 'Thu: 6am - 1am\n' + 'Fri: 6am - 11pm\n' + 'Sat: 8am - 11pm\n'

def gym_open_or_closed(hours, day_of_week):
        if(day_of_week < 6 and hours >= 6):
            if(day_of_week == 4 and hours > 23):
                return False
            else:
                return True
        elif(day_of_week > 4 and hours >= 8):
            if(day_of_week == 5 and hours > 23):
                return False
            else:
                return True
        else:
            return False

def text_to_voice_url(answer_to_say):
	speak = ''
	for letter in answer_to_say:
		if(letter == ' '):
			speak = speak +'%20'
		else:
			speak = speak + letter
	return 'http://tts-api.com/tts.mp3?q=' + speak

def parse_audio(audio):
    if 'football' in audio:
        print("true")
        print(get_football_info(audio))
    if 'rsf' in audio or 'gym' in audio:
        return gym_info(audio)

def answer(audio):
    return parse_audio(audio) 




