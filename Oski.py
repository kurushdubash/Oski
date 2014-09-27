import speech_recognition as sr
r = sr.Recognizer(language = "en-US", key = "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
r.energy_threshold = 500
r.pause_threshold = 0.5
with sr.Microphone() as source:                # use the default microphone as the audio source
    print("Listening...")
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    print("Transcribing")
try:
    print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")