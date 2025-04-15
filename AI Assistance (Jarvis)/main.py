"""speak function"""
#inbuilt voices
import pyttsx3
import os
import wikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[2].id)
engine.setProperty('rate', 170)

#print(voices[2].id)

def def_speake(audio):
    print(f"  Jarvis : {audio}")
    engine.say(audio)
    engine.runAndWait()

#def_speake("Are you ok!")

"""how to add google assistance voice:"""
# from gtts import gTTS
# import os
# def google_assistance_speake(audio):
#     print()
#     print(f"Google Assistant: {audio}")
#     kk = gTTS(audio, lang="en", slow= False)
#     kk.save("Assis.mp3")
#
#     from playsound import playsound
#     playsound("Assis.mp3")
#     os.remove("Assis.mp3")  #optional
#
# google_assistance_speake("Hello sir, How are you?")

"""adding external voices:""" #->>> https://ttsmp3.com/
from playsound import playsound
def ex_speake(path):
    playsound(path)

#-----------------------------------------------------------

"""speech recognition"""
#goto ->>cmd ->> pip install speechrecognition

import speech_recognition as sr
#taking command and listen

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(": Recognizing...")
        query = r.recognize_google(audio, language="en-US", show_all=False)
        print(f": your command: {query}\n")

    except:
        print("Say that again please...")
        return "None"
    return query


#------------------------------------------------------

import webbrowser as web

if __name__ == "__main__":
    ex_speake("G:\\Jarvis\\Database\\Voices\\1_Emma.mp3")
    # ex_speake("G:\\Jarvis\\Database\\Voices\\1_Brian.mp3")

    def Task_exe():
        while True:
            query = takeCommand().lower()

            if "open google" in query:
                web.open("https://www.google.com/")

            elif "what is your name" in query:
                def_speake("My name is jarvis. I was created by Zilane.")

            elif "set alarm" in query:
                from features import Alarm
                Alarm(query)

            elif "temperature" in query:
                from features import Temerature
                Temerature(query)

            elif "calculate" in query:
                from features import Calculator
                Calculator(query)

            elif "download" in query:
                from features import DownloadYoutube
                DownloadYoutube()



            elif "google" in query:
                from features import Google_search
                Google_search(query)

            elif "open youtube" in query:
                web.open("https://www.youtube.com/")

            elif "youtube" in query:
                from features import youTubeSearch

                Q1 = query.replace("jarvis", "")
                Q2 = Q1.replace("search", "")
                Q3 = Q2.replace("in", "")
                Q4 = Q3.replace("youtube", "")
                Q5 = Q4.replace("about", "")
                youTubeSearch(Q5 or Q4)

            elif "wikipedia" in query:
                from features import Wikipedia
                Q = Wikipedia(query)
                def_speake("Do you want see info in wikipedia?")
                respons = takeCommand().lower()
                if "yes" in respons or "yes" == respons:
                    res = "https://en.wikipedia.org/wiki/" + Q
                    web.open(res)

                elif "no" in respons:
                    def_speake("okey sir")

            elif "favourite song" in query:
                from features import fav_song_vid
                fav_song_vid("fs")
            elif "jarvis stop" in query:
                def_speake("Alright sir")
                break



    Task_exe()


