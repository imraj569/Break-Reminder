import pyttsx3
from time import sleep
import schedule,os
import random

#text to speech
def speak(audio):
    engine = pyttsx3.init('sapi5')
    #change the voices
    voices = engine.getProperty('voices') 
    engine.setProperty('voice',voices[1].id)
    #change speech rate
    engine.getProperty("rate")
    engine.setProperty("rate",190)
    engine.say(audio)
    engine.runAndWait()

def Breaks_Reminder():
    file_path = ["Database\\break.jpg","Database\\break1.jpg","Database\\break2.jpg","Database\\break3.jpg"]
    message = random.choice(file_path)
    os.startfile(message)
    break_messages = ["boss its time to take a break","boss its 25 minutes since you are working please take a mini break","boss please take a mini break"]
    speak(random.choice(break_messages))

if __name__ == "__main__":
    speak("Break reminder started boss")
    schedule.every(25).minutes.do(Breaks_Reminder)
    while True:
        schedule.run_pending()
        sleep(1)