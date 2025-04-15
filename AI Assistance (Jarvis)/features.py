import pyperclip
import pywhatkit
import wikipedia
#from pywhatkit import WikiHow, search_wikihow
import os
import webbrowser as web
from main import takeCommand

import wolframalpha
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[2].id)
engine.setProperty('rate', 170)
def def_speake(audio):
    print()
    print(f"Jarvis : {audio}")
    print()
    engine.say(audio)
    engine.runAndWait()

def youTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    def_speake("This is what I found sir.")
    #pywhatkit.playonyt(term)

def fav_song_vid(term):
    if term == "fs":
        result = "https://www.youtube.com/watch?v=Hxe362w66GI"
        web.open(result)
        def_speake("It is also my favorite song sir.")

def Wikipedia(term):
    global Query
    try:
        def_speake("searching in wikipedia")
        Query = term.replace("jarvis ", "")
        Query = Query.replace("search ", "")

        Query = Query.replace("tell me about ", "")
        Query = Query.replace("tell me ", "")
        Query = Query.replace("about ", "")
        Query = Query.replace("in wikipedia", "")
        Query = Query.replace("with the help of ", "")
        Query = Query.replace("wikipedia", "")
        Query = Query.replace("can you help me ", "")
        #print(Query)

        results = wikipedia.summary(str(Query), sentences=1)
        def_speake("According to wikipedia")
        def_speake(results)

        return Query
    except Exception:
        def_speake("sorry. There is some error")
        return Query

def Google_search(term):
    query = term.replace("what is", "")
    query = query.replace("jarvis", "")
    query = query.replace("How to", "")
    query = query.replace("what do you mean by", "")
    query = query.replace("tell me about", "")
    query = query.replace("tell me","")
    query = query.replace("in google", "")
    query = query.replace("google", "")
    query = query.replace("with the help of", "")
    query = query.replace("through", "")
    Query = str(query)
    pywhatkit.search(Query)


def Alarm(query):
    time_here = open("G:\\Jarvis\\alarm_data.txt", "a")
    time_here.write(query)
    time_here.close()
    #os.startfile("G:\\Jarvis\\alarm\\alarm.py")
    import runpy
    runpy.run_path("G:\\Jarvis\\alarm\\alarm.py")


def DownloadYoutube():
    try:
        from pytube import YouTube
        from pyautogui import click
        from pyautogui import hotkey
        from pyperclip import paste
        from time import sleep
        sleep(2)
        click(x=462, y=72)
        hotkey("ctrl", "c")
        value = pyperclip.paste()

        hd_value = value.replace("https://www.", "https://www.ss")
        web.open(hd_value)
        sleep(10)

        click(x=493, y=723)
        click(x=960, y=731)
        click(x=493, y=723)
        click(x=960, y=731)
        sleep(10)
        click(x=493, y=723)
        click(x=960, y=731)

        link = str(value)

        def Download(linkk):
            url = YouTube(linkk)
            video = url.streams.first()
            video.download("G:\\Jarvis\\Database\\Youtube_downloaded_video")

        def_speake("do you want to download it in low quality?")
        if "yes" in takeCommand().lower():
            Download(link)
            def_speake("Done sir, I have downloaded the video.")
            def_speake("Here it is")
            os.startfile("G:\\Jarvis\\Database\\Youtube_downloaded_video")
        else:
            def_speake("Ok sir")
    except Exception:
        def_speake("Sir, somthing went wrong!!")

#------------------------------------------------------------
def wolframAlpha(term):
    api_key = "WU253U-R3GPYXTXJ7"
    requester = wolframalpha.Client(api_key)  # will give a  database
    requested = requester.query(term)   # to get result

    try:
        answer = next(requested.results).text  # will give the result in text format
        return answer
    except:
        def_speake("An string is not answerable")

def Calculator(term):
    Term = str(term)

    Term = Term.replace("jarvis ", "")
    Term = Term.replace("calculate ", "")

    Term = Term.replace("multiply ", "*")
    Term = Term.replace("plus ", "+")
    Term = Term.replace("minus ", "-")
    Term = Term.replace("divided by ", "/")
    Term = Term.replace("divide ", "/")
    Term = Term.replace("into ", "*")
    Term = Term.replace("exponent ", "e")
    Term = Term.replace("to the power ", "^")

    final = str(Term)
    try:
        result = wolframAlpha(final)
        def_speake(f" the calculated value = {result}")
    except:
        def_speake("An string is not answerable")


def Temerature(term):
    Term = str(term)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("temperature of ", "")
    Term = Term.replace("temperature in ", "")
    Term = Term.replace("temperature ", "")
    #Term = Term.replace("in ", "")
    #Term = Term.replace("what is the temperature of ", "")
    Term = Term.replace("what is the ", "")

    query = str(Term)
    if "outside" in query:
        v1 = "temperature in bangladesh"
        answer = wolframAlpha(v1)
        def_speake(f"{v1} is {answer}")

    else:
        v2 = "temperature in " + query
        answer = wolframAlpha(v2)
        def_speake(f"{v2} is {answer}")


#-----------------------------------------------------------------