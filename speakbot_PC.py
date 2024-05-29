import pyttsx3
import speech_recognition as sr
import datetime
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import os
import pyjokes
import pyautogui
import news
import operator


engine = pyttsx3.init('sapi5')     # sapi5 is the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    
    if hour >= 0 and hour < 12:
        speak(f"Good Morning! its {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon! its {tt}")
    else:
        speak(f"Good evening! its {tt}")

    speak("I am your Personal Assistant. Please tell me how may I help you?")

def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()

    while True:

        query = takeCommand().lower()

# get information through wikipedia
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            speak(results)
            print(results)

# open google command
        elif 'open google' in query:
            speak("Sir, what should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

# open youtube command
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("Sir, what should I search on youtube")
            ab = takeCommand().lower()
            webbrowser.open(f"{ab}")

# play song in youtube command
        elif 'play song in youtube' in query:
            kit.playonyt("sanam re")

# open notepad command
        elif 'open notepad' in query:
            npath = "C:\\Users\\ankit\\OneDrive\\Desktop\\Notepad.lnk"
            os.startfile(npath)

# open vs code command
        elif 'open vs code' in query:
            npath = "C:\\Users\\ankit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(npath)

# to close any application, follow the procedure:
        elif 'close notepad' in query:
            speak("Okay Sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

# open command prompt procedure:
        elif 'open command prompt' in query:
            os.system("start cmd")

# play music from your directory file
        elif 'play music' in query:
            music_dir = "C:\\Users\\ankit\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

# getting your ip address
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

# opening facebook using webbrowser module
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

# opening instagram command
        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

# open linkedin command 
        elif 'open linkedin' in query:
            webbrowser.open("www.linkedin.com")

# open web browser- chrome command
        elif 'open chrome' in query:
            webbrowser.open("www.chrome.com")

# sending message to a number procedure
        elif 'send message' in query:
            kit.sendwhatmsg("+919399440805", "hi", 11, 53)

# to find a joke using pyjokes module
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

# command for shutting down your system
        elif 'shut down the system' in query:
            os.system("shutdown /r /t 5")

# sleep command to sleep your system
        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
# switch the window command helps switching from one desktop to another
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

# getting news from internet
        elif 'tell me news' in query:
            speak("please wait sir, fetching the latest news")
            news()

# calculation command procedure
        elif 'do some calculations' in query or "can you calculate" in query:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 3 plus 3")
                    print("listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        '/' : operator.__truediv__,
                    }[op]
            
                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))

            except Exception as e:
                print(e)
                speak("Sorry, the calculation isn't performed")

# no thanks command to exit the program
        elif 'no thanks' in query:
            speak("thanks for using me Sir, have a nice day")
            sys.exit()


        speak("Sir, May I do something for you...")
