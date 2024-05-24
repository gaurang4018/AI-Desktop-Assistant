import pyttsx3
import speech_recognition as sr
import datetime
from datetime import *
import wikipedia
import webbrowser
import os
from playsound import playsound
from pytube import YouTube
from pyautogui import hotkey
from pyperclip import paste
from time import sleep
import pyautogui
import subprocess
import wolframalpha
import gui
from gui import *
import asyncio
import tkinter as tk

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate",180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)
    
    try:
        print("Recognizing") 
        query = r.recognize_google(audio,language="en-in")
        
    except Exception as e:
        print(e)    
        return "None"    
    return query    




def time():
    timeStr = str(datetime.now().strftime("%H:%M:%S"))
    speak(f"The time currently is {timeStr}")
    
    
def googleSearch(query):
    query = query.replace("google search","")
    query = query.replace("ghost","")
    query = query.replace("search","")
    query = query.replace("google","")
    query = str(query).strip()
    print(query)
    try:
        # wikipedia.search(query)
        result = wikipedia.summary(query,2)
        speak("This is what I found on web")
        speak(result)
    except:
        speak("Sorry! no results found")    

def youtubeSearch(query):
    term = query.replace("youtube search"," ")
    term = query.replace("youtube"," ")
    term = query.replace("Ghost"," ")
    term = query.replace("open youtube"," ")
    
    if term != " ":
        result = "https://www.youtube.com/results?search_query=" + term
        try:
            webbrowser.open(result)
            speak("This might help you")
        except:
            webbrowser.open("www.youtube.com")
    else:
        webbrowser.open("www.youtube.com")
        speak("opening youtube")           


cmd = (["python","D:\\project-ghost\\additional programs\\Alarm\\Alarm.py"])        
def alarm(query):
    Timehere = open("D:\\project-ghost\\database\\alarm-data.txt","a")
    Timehere.write(query)
    Timehere.close()    
    speak("Alarm set")
    try:
        global p1
        p1 = subprocess.Popen(cmd)
        
    except:
        speak("Sorry, something went wrong")

# Stopping alarm beep
def stopAlarm():
    p1.terminate()
    p1.wait()

            
def youtubeVideoDownload():
    value = ""
    speak("Select link")
    sleep(1)
    linkPosition = pyautogui.position() 
    sleep(1)
    hotkey("ctrl","c")
    value = paste()
    
    Link = str(value)
    print(Link)
    
    
    def DownloadVid(link):
        
        try:
            yt = YouTube(link)
            streams = yt.streams.get_highest_resolution()
            speak("Downloading Video")
            streams.download("D:\\project-ghost\\database\\youtube-videos")
            speak("Video Downloaded")
        except:
            speak("Sorry ! try again")    
        
        

    DownloadVid(Link)       

def wolfram(query):
            # API key
        apikey = "X8855R-RPKG7TY2UW"
        requestor = wolframalpha.Client(apikey)
        res = requestor.query(query)
        
        try:
            answer = next(res.results).text
            speak(answer)
        except:
            speak("Sorry! Try again")    
    
def calculator(query):
    term = str(query) 
    term = term.replace("ghost","")
    term = term.replace("sum","+")
    term = term.replace("plus","+")
    term = term.replace("multiply","*")
    term = term.replace("minus","-")
    term = term.replace("divide","/")
    
    try:
        finalResult = wolfram(query)
        speak(finalResult)
    except:
        speak("Sorry ! Try again")    
        return
        
def temperature(query):   
    try:
        term = str(query)
        term = term.replace("ghost",'')
        term = term.replace("tell",'')
        term = term.replace("me",'')
        
        result = wolfram(term)
        speak(f"Temperauture  {result}")
    except:
        speak("Sorry! Try again")    
        return
        
  

def createFile():
    try:
        speak("Tell me what to write")
        notes = listen()
        
        time = (datetime.now().strftime("%H:%M"))
        filename = str(time).replace(":","-") + "-note.txt"

        with open(filename,"w") as file:
            file.write(notes)
 # type: ignore
        path_1 = "D:\\project-ghost\\" + str(filename)
        path_2 = "database\\note-files\\" + str(filename)

        os.rename(path_1,path_2)
        os.startfile(path_2)
    except:
        speak("Sorry! Try again")
        return

    
# async funtion to enable the rename button at the right time
async def enableRenameButton():
    await asyncio.sleep(0.1)
    renameButton.config(state=NORMAL)
    selected_folder.place(x=20,y=30)
    renameInput.place(x=20,y=95)
    renameButton.place(x=420,y=93)
    files_list.place(x=20,y=140)
    
    
    
    
async def enableDeleteButton():
    await asyncio.sleep(0.1)
    deleteButton.config(state=NORMAL)
    selected_folder.place(x=20,y=30)
    deleteButton.place(x=420,y=93)
    files_list.place(x=20,y=140)