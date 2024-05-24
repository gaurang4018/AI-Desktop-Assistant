import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from features import *
import os
from openAi.bot import *
import tkinter as tk
from gui import *
import asyncio
import multiprocessing


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
    
def greet():
    
    hour = int(datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning !")
    elif hour>=12 and hour<=16:
        speak("Good afternoon !")
    else:
        speak("Good evening !")  
    speak("I am Ghost! please tell me How may I help You !")     
    
    
async def MainBrain():
    
    # Greeting and introduction
    greet()
    
    while True:
        # Taking user command
        query = str(listen()).lower()
        print(query)
        
        saveQuery = open("database\\user-query-data.txt","a")
        saveQuery.writelines(f"user-query: {query}\n")
        saveQuery.close()
        
        # matching command terms
        
        if "google search" in query :
            googleSearch(query)
        
        elif "turn off" in query:
            speak("Thanks for your time! Good Byee  ")
            return 1
        
        elif "time" in query:
            time()     
            
        elif "youtube search" in query or "open youtube" in query or "youtube" in query:
            youtubeSearch(query)       
        
        elif "set alarm for" in query or  "set alarm" in query or "alarm" in query:
            alarm(query)
            
        elif  "quit" in query or "close alarm"  in query or "close" in query or "stop" in query:
            stopAlarm()            
            
            
        elif "download this video" in query or "download video" in query or "download" in query:
            youtubeVideoDownload()            
        
        elif "temperature" in query:
            temperature(query)
         
        elif "calculate" in query:
            calculator(query) 
        
        elif "open file" in query:
            path = str(selected_folder.cget("text")+"/"+os.listdir(selected_folder.cget("text"))[0])
            print(path)
            os.startfile(path)
            
        elif "play video" in query:
            try:
                path = str(selected_folder.cget("text")+"/"+os.listdir(selected_folder.cget("text"))[0])
                print(path)
                os.startfile(path)
            except:
                speak("select a folder first")    
            
        elif "play music" in query:
            try:
                path = str(selected_folder.cget("text")+"/"+os.listdir(selected_folder.cget("text"))[0])
                print(path)
                os.startfile(path)  
            except:
                speak("select a folder first")   
            
        elif "create file" in query or "create new file" in query or "create a file" in query:
            createFile()    
            
        elif "log off" in query or "sign out" in query or "shutdown" in query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])    
            
        elif "rename file" in query or "rename" in query:
            await enableRenameButton()
            speak("select the file to rename, write the new name and press rename button")
            break
        
        elif "delete file" in query or "delete" in query:
            await enableDeleteButton()
            speak("select the file to delete and press delete button")
            break
      
        else:
            if chatGptClone(query) != "None":
                speak(chatGptClone(query))
                        
                        
# GUI code 
# start button
button1 = Button(leftFrame,text="Start",font=("Tahoma", 15),fg="#1c1c1e", justify="center",background="#fffc00",width=13,height=1 ,anchor="center",cursor="hand2",command=lambda: asyncio.run(MainBrain()))
button1.place(x=20,y=350)

if __name__ == "__main__":

    root.mainloop() 
          
    