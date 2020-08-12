import pyttsx3 #text to speech library
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):#this function take audio as a agruement
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and  hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    elif hour>18 and hour<20:
        speak("Good evening")
    elif hour>20 and hour<24:
        speak("Good night")
    speak("I am jarvis sir how may i help you ")

def takecommand():
    #It takes microphone input from the user and returns the string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening==")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing==")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say it again please")
        return "None"
    return query


if __name__ == "__main__":
    #speak("I am a jarvis and i love iron man")
    wish()
    while True:
        query=takecommand().lower()#logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(f'{query}',sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"Mam the time is {strTime}")
            print(strTime)
        elif 'open code' in query:
            codepath = "C:\\Users\\vidhi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'quit' in query:
            speak("Thanku sir,jarvis is quitting")
            


    