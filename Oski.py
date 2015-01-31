# import speech_recognition as sr
import requests
from datetime import datetime


# def get_audio():
#     r = sr.Recognizer(language = "en-US", key = "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
#     r.energy_threshold = 1800
#     r.pause_threshold = 0.5
#     with sr.Microphone() as source:                # use the default microphone as the audio source
#          print("Listening...")
#          audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
#     try:
#         print("Transcribing..")
#         transcribed_audio = r.recognize(audio)   # recognize speech using Google Speech Recognition
#         if(transcribed_audio == ''):
#             print("Could not understand audio") # speech is unintelligible 
#             print("Trying again.")
#             return get_audio()
#         return transcribed_audio
#     except LookupError:                            
#         print("Could not understand audio") # speech is unintelligible 
#         print("Trying again.")
#         return get_audio()

def get_football_info(audio):
    """ GETs College Football JSON data, and returns the dictionary """
    football_api_url = 'http://api.sportsdatallc.org/ncaafb-t1/2014/REG/schedule.json?api_key=6r45ruu32nbydywtds97krap'
    football_data = requests.get(football_api_url)
    football_dict = football_data.json()
    return football_dict

def gym_info(audio):
    """ Listens to audio, and returns either the Gym Schedule, or whether the Gym is open or closed """
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
    return get_gym_schedule()
    
def bear_walk(audio):
    """ Listens to the audio, and returns the phone number of Bear Walk"""
    if 'bear' in audio or 'walk' in audio:
        return 'Contact Bear Walk at 510 642 9255'

def bear_trasit(audio):
    """ Listens to the audio, and returns the phone number of Bear Walk"""
    if 'bear' in audio or 'walk' in audio:
        return 'Contact Bear Walk at 510 642 9255'

def next_football_game(audio):
    """ Listens to audio, and returns the next CAL football game"""
    if 'football' in audio or 'game' in audio:
        return 'Our next football game is on October 4 at Washington State at 7 30 P M'

def library_hours(audio):
    """ Listens to audio, and returns if the library is open"""
    if 'library' in audio or 'today' in audio:
        return 'Mofitt closes at 10 P M'


def get_gym_schedule():
    """ Returns the string containing the GYM week schedule """
    return 'Sun: 8am - 1am\n' + 'Mon: 6am - 1am\n' + 'Tue: 6am - 1am\n' + 'Wed: 6am - 1am\n' + 'Thu: 6am - 1am\n' + 'Fri: 6am - 11pm\n' + 'Sat: 8am - 11pm\n'

def gym_open_or_closed(hours, day_of_week):
    """ Uses current time, and determines if the Gym is currently open or not.
    Returns True for open, and false for closed"""
    print(hours)
    print(day_of_week)
    if(day_of_week < 6 and hours >= 6 and day_of_week != 5):
        if(day_of_week == 4 and hours > 23):
            return False
        else:
            return True
    elif(day_of_week > 4 and hours >= 8):
        print
        if(day_of_week == 5 and hours >= 23):
            return False
        else:
            return True
    else:
        return False

def get_date():
    time_info = datetime.today()
    return time_info.strftime("%A %d. %B %Y")

def get_time():
    time_info = str(datetime.today());
    for char in str(time_info):
        if(char == ' '):
            time_info = time_info[1:]
            break
        else:
            time_info = time_info[1:]
    hours = ''
    for char in time_info:
        if(char != ':'):
            hours = hours + char
            time_info = time_info[1:]
        else:
            break
        if (int(hours) > 12):
            hours = int(hours) - 12
        minutes = ''
        for char in time_info:
            if(char != ':'):
                minutes = minutes + char
            else: 
                break
    return str(hours) + " " + minutes

def hey_oski(audio):
    if 'hey' in audio or 'oski' in audio:
        return "Hey Kurush, you're an idiot"
    return 'h'

def text_to_voice_url(answer_to_say):
    speak = ''
    for letter in answer_to_say:
        if(letter == ' '):
            speak = speak +'%20'
        else:
            speak = speak + letter
    return 'http://tts-api.com/tts.mp3?q=' + speak

def parse_audio(audio):
    if 'rsf' in audio or 'gym' in audio:
        return gym_info(audio)
    if 'bear' in audio or 'walk' in audio:
        return bear_walk(audio)
    if 'football' in audio or 'game' in audio:
        return next_football_game(audio)
    if 'library' in audio:
        return library_hours(audio)
    if 'date' in audio or 'today' in audio:
        return get_date()
    if 'time' in audio:
        return get_time()
    if 'hey' in audio or 'oski' in audio:
        return hey_oski(audio)
    return 'I was no help'

def answer(audio):
    return parse_audio(audio) 




