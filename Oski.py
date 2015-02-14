# import speech_recognition as sr
import requests
from datetime import datetime
# import wit

# wit_access_tokem = "DZOBQMEV7MX65IUV4VQGS4HQCUTFAWRJ"
weather_api = '2ffd40362f6c4bdd050c1ad48eaa7891cb1e4890'

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
    date_info = str(datetime.now().date().isoformat())
    stringer = "today is the {0} of {1} in {2}".format(date_info[8:9], date_info[5:6], date_info[0:4])
    return stringer  # YYYY-MM-DD

def get_time():
    time_data = datetime.now().time().isoformat();
    hour = int(time_data[0:2])
    minute = time_data[3:5]
    light = 'AM'

    if hour > 12:
        hour = hour - 12
        light = 'PM'
    elif hour == 00:
        hour = 12
    return "it is {0}:{1} {2}".format(str(hour), str(minute), light)

def hey_oski(audio):
    if 'hey' in audio or 'oski' in audio:
        return "Hey Kurush, you're an idiot"
    return 'Stanford Sucks'

def get_weather(audio):
    zip_code = 94709
    weather_url = 'http://api.worldweatheronline.com/free/v1/weather.ashx?q=' + str(zip_code) + '&format=json&num_of_days=5&key=' + str(weather_api)
    weather_data = requests.get(weather_url)
    weather_josn = weather_data.json()
    date_obj = datetime.now().date().isoformat()
    year = date_obj[0:4]
    month = date_obj[5:7]
    day = date_obj[8:10]

    if "today" in audio:
        if "high" in audio:
            forcast = weather_josn['data']['weather'][0]['tempMaxF']
            return "The high for today is {0}".format(str(forcast))
        elif "low" in audio:
            forcast = weather_josn['data']['weather'][0]['tempMinF']
            return "The low for today is {0}".format(str(forcast))
        else:
            forcastmin = weather_josn['data']['weather'][0]['tempMinF']
            forcastmax = weather_josn['data']['weather'][0]['tempMaxF']
            return "It is going to be between {0} to {1} degrees fahrenheit today".format(forcastmin, forcastmax)
    elif "tomorrow" in audio:
        if day < 30:
            nextDay = day + 1
        else: 
            nextDay = 1
            month = month + 1
        tomorrowDate = "{0}-{1}-{2}".format(year, month, nextDay)

        forcastmin = weather_josn['data']['weather'][str(time_data)]['tempMinF']
        forcastmax = weather_josn['data']['weather'][str(time_data)]['tempMaxF']
        return "It is going to be between {0} to {1} degrees fahrenheit tomorrow".format(forcastmin, forcastmax)
    else:
        forcast = weather_josn['data']['current_condition'][0]['temp_F']
        return "It is {0} degrees right now".format(str(forcast))

def text_to_voice_url(answer_to_say):
    speak = ''
    for letter in answer_to_say:
        if(letter == ' '):
            speak = speak +'%20'
        else:
            speak = speak + letter
    return 'http://tts-api.com/tts.mp3?q=' + speak

def parse_audio(audio):
    # wit.init()
    # response = wit.text_query(audio, wit_access_tokem)
    if 'rsf' in audio or 'gym' in audio:
        return gym_info(audio)
    if 'bear' in audio or 'walk' in audio:
        return bear_walk(audio)
    if 'football' in audio or 'game' in audio:
        return next_football_game(audio)
    if 'library' in audio:
        return library_hours(audio)
    if 'date' in audio:
        return get_date()
    if 'time' in audio:
        return get_time()
    if 'hey' in audio or 'oski' in audio:
        return hey_oski(audio)
    if "weather" in audio or "hot" in audio or "cold" in audio:
        return get_weather(audio)
    return 'I was no help'

def answer(audio):
    return parse_audio(audio) 





