import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    """This function is used to speak. It will take speak and greeting you"""

    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """This function is used for wish to user"""

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am your personal Assistant Sir! Please tell me How may I help you?")

def takeCommand():
    """It takes microphone input from the user and return string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print("say that again pleases.....")
        return "None"
    return query

def sendEmail(to, content):
    """This will send email to another person"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    file = open("E:\\Projects\\PersonalAssistant\\p.txt", 'r')
    mail_id = file.readline().strip("\n")
    password = file.readline().strip("\n")
    server.login(mail_id, password)
    server.sendmail(mail_id, to, content)
    server.close()
    file.close()
    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            numberOfFiles = len(songs)
            print(songs)
            song_num = random.randint(0, numberOfFiles - 1)
            os.startfile(os.path.join(music_dir, songs[song_num]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\prabh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to prabhakar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "B@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry! I am not able to send this email.")
        
        elif 'exit' in query:
            speak("Thank you sir! Have a nice day sir.")
            exit()






