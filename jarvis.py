import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import comtypes.client
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
        
    else:
        speak("good evening")
        
    speak("i am jarvis , please help me")
    
def takecommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("listening")
         r.pause_threshold = 1
         audio = r.listen(source)
     try:
        print("recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
        
     except Exception as e:
        print("say that again please")
        return None
     return query
if __name__=="__main__":
    wishme()
    while True:
         query = takecommand().lower()
         if 'wikipedia' in query:
             speak('searhing wikipedia')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("according to wikipedia")
             print(results)
             speak(results)
             
         elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
            speak("youtube is opened")
        
         elif 'open google' in query:
            webbrowser.open('google.com')
            
         elif 'play music' in query:
            webbrowser.open('spotify.com')             
     
                

