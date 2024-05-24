import os
import datetime
from playsound import playsound




extractedTime = open("D:\\project-ghost\\database\\alarm-data.txt","rt")
time = extractedTime.read()
Time = str(time)

deleteTime = open("D:\\project-ghost\\database\\alarm-data.txt","r+")
deleteTime.truncate(0)
deleteTime.close()

def ringAlarm(time):
    timeToSet = str(time)
    timeToSet = timeToSet.replace("ghost"," ")
    timeToSet = timeToSet.replace("set alarm for"," ")
    timeToSet = timeToSet.replace("set"," ")
    timeToSet = timeToSet.replace("alarm"," ")
    timeToSet = timeToSet.replace("for"," ")
    timeToSet = timeToSet.replace(" and ",":")
    
    alarmTime = str(timeToSet).strip()
    
    
    while True:
          
        currentTime = str(datetime.datetime.now().strftime("%H:%M"))
        # print(currentTime,"and",alarmTime)
        if currentTime == alarmTime:
           
            playsound("additional programs\\Alarm\\alarmRingtone.mp3")

            
        elif currentTime > alarmTime:
            break   

ringAlarm(Time)


        