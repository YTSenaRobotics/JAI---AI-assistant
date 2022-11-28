import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import pywhatkit

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voice', voices[0].id)


def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print("    ")
    Assistant.runAndWait()

def Takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)



    try:
        print("Recognising")
        query = command.recognize_google(audio, languages='en-in')
        print("You said:", query)


    except Exception as Error:
        return "none"


Speak("Hello sir, I am jai")
Takecommand()
