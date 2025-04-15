
from playsound import playsound
import os
import datetime
extracted_time = open("G:\\Jarvis\\alarm_data.txt", "rt")
time = extracted_time.read()
Time = str(time)

os.stat("G:\\Jarvis\\alarm\\alarm.py")
delete_time = open("G:\\Jarvis\\alarm_data.txt", "r+")
delete_time.truncate(0)
delete_time.close()

def Ring_now(time):
    time_to_set = str(time)
    time_now = time_to_set.replace("jarvis ", "")
    time_now = time_now.replace("set alarm for ", "")
    time_now = time_now.replace("set alarm at ", "")
    time_now = time_now.replace("set alarm ", "")
    time_now = time_now.replace("set ", "")
    time_now = time_now.replace("alarm ", "")
    time_now = time_now.replace("o'clock ", "")
    time_now = time_now.replace("clock ", "")
    time_now = time_now.replace("and", ":")
    #time_now = time_now.replace("", "")
    alarm_time = str(time_now)

    while True:
        current_time = str(datetime.datetime.now().strftime("%H : %M"))
        if current_time == alarm_time:
            print("Sir alarm is ringing!!!")
            playsound("G:\\Jarvis\\alarm\\1.mp3")

        elif current_time > alarm_time:
            break

Ring_now(Time)


