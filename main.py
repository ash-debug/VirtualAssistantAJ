import pyttsx3
import datetime
import pyautogui
from pywikihow import search_wikihow


import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import pywhatkit as kit
import geocoder
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Ashu Sir , my name is AJ, how should i help you")
    elif  hour>=12 and hour<=18:
        speak("Good Afternoon Ashu Sir , my name is AJ, how should i help you")
    else:
        speak("Good Evening Ashu Sir , my name is AJ, how should i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
 #       print(e)
        speak("sorry sir i didn't here you , please pardon")
        return "none"
    return query






if __name__ == '__main__':
#    speak("Ashu is a good boy")
     wishme()
     while True:
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            results = wikipedia.summary(query , Sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'volume up' in query:

            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'activate how to do mod' in query:
            speak("how to do is activated , please tell me what do you want to know")
            while True:
                speak("tell me what you want to know")
                how=takeCommand()
                try:
                    if "exit" in how or "close" in how:

                        speak("okay sir , how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir , i am not able to find the results")

        elif "battery of lapop"  in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir  , our system has {percentage} percent of battery")
            if percentage>=75:
                speak("sir , we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                speak("sir , battery is sufficient")
            elif percentage<=40:
                speak("sir , battery is low , we dont have enough power to continue with our work , please connect to charging ")
            elif percentage<=20:
                speak("sir , we have very low power , connect our system with charging as soon as possible")

        elif "space" in query:
            import psutil
            mem = psutil.cpu_stats()
            print(mem)

        elif "cpu usage" in query:

            import psutil

            print('The CPU usage is: ', psutil.cpu_percent(4))
            print('RAM memory % used:', psutil.virtual_memory()[2])
            




        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir , what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open("f{cm}")
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open android studio' in query:
            codepath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(codepath)

        elif 'close the pc' in query:
            codepath="C:\\Users\\ashu0\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\shutdown"
            os.startfile(codepath)

        elif 'open whatsapp' in query:
            codepath="C:\\Users\\ashu0\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codepath)

        elif 'open bluejay' in query:
            codepath="C:\\Program Files\\BlueJ\\BlueJ.exe"
            os.startfile(codepath)

        elif 'open notepad' in query:
            codepath="C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2204.12.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(codepath)

        elif 'open cmd' in query:
            os.system("start cmd")

        elif 'play songs in youtube' in query:
            speak("which song should i play sir")
            kit.playonyt("let me love you")

        elif 'what is my location' in query:

            g =geocoder.ip('me')
            City=g.city
            speak(f"sir i think we are in {City}")
            speak("any other work sir?")




        elif 'you can quit' in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        elif 'yes' in query:
            speak("what's that work")

        #elif 'close notepad' in query:
         #   speak("okay sir , closing notepad")
          #  os.system("taskkill /f /im notepad.exe")

#        elif ' close whatsapp' in query:
 #           speak("okay sir , closing whatsapp")
  #          os.system("taskkill /f /im whatsapp.exe")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")












