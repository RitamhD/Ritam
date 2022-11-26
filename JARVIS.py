import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import sys
import glob
import random
import playsound
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[2].id)
engine.setProperty('rate',200)

'''for voice in voices:
    print(voice.id)
    engine.setProperty('voice',voice.id)
    engine.say('hello sir')
engine.runAndWait()'''



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif 12<hour<16:
        speak('Good Afternoon')
    elif 16<=hour<=20:
        speak('Good Evening')
    else:
        speak('Its night time, but Mikki is online!')
    speak('How may I help you sir?')
wishMe()


def takeCommand():
    # It takes microphone input from user and return string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print('...recognising...')
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        speak("Could you say that again please...")
        return "None"
    return query

# def create_playlist(path):
#     for song in glob.glob(path):
#         print('Now Playing...'+song)
#         playsound(song)

def taskExecution():

    while True:

        query = takeCommand().lower()

        if 'hello' in query:
            speak('Hello Sir! do you need any help?')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=1)

            speak('Ok, here what I got, according to Wikipedia,')
            print(results)
            speak(results);speak('Anything else sir?')
        
        elif 'open youtube' in query:
            speak('Ok!')
            webbrowser.open('https://www.youtube.com/')
            speak('Anything else sir?')
        elif 'anime' in query:
            speak('Ok!')
            webbrowser.open('https://www.gogoanime.lu/')
            speak('Anything else sir?')
        elif 'browser' in query:
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)
            speak('Anything else sir?')
        elif 'music' in query:
            speak('How about this song!')
            music_dir = "C:\\Users\\LENOVO\\OneDrive\\Documents\\My music\\Anime"
            songs = os.listdir(music_dir)
            n = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[n]))
            break
        # elif 'song' in query:
        #     speak('How about this song!')
        #     playsound("Slow Dance - SUNEOHAIR (Español English)(wally_works).mp3")
        
        elif 'sleep' in query:
            speak('As you say, shutting down')
            break
        elif 'no thanks' in query:
            speak('Ok sir')
            break
        elif 'good night' in query:
            speak('Good night sir, sleep well, See you tomorrow!')
            os.system('taskkill /f /im code.exe')
            
        else:
            speak("Sorry I don't understand, I am still learning, but if you want I can play some music for you, just say play a music")
taskExecution()