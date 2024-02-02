import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib
import pywhatkit
import openai
from apikey import api_data

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def play_on_youtube(video):
    pywhatkit.playonyt(video)
def search_on_google(query):
    pywhatkit.search(query)
def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('supriyo874@gmail.com', '9933697745')
    server.sendmail('supriyo874@gmail.com', to, content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")


    elif hour>12 and hour<18:
        speak("Good Afternoon")


    else:
        speak("Good Evening!")


    speak("I am jarvis Sir. Please tell how mai I assist you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognize...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")



    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'stop' in query:
            break


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")



        elif 'spotify' in query:
            webbrowser.open("spotify.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = takeCommand().lower()
            search_on_google(query)
        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:S")
            speak(f"Sir, the time is {strTime}")
        elif 'email to john' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "supriyo874@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")














