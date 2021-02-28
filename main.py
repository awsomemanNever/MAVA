import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

def main():
    
    while True:
        recognise()

def recognise() : 

    with sr.Microphone() as source:
        print("listening")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        
        command = command.lower()
        command = command.split(" ")
        
        
        if 'monday' == command[0]:
            command.pop(0) 
            command = "".join(command)

            if "play" in command:
                play(command)

            elif "time" in command:
                time(command)
                
            
            
def play(command): 
    command.pop(0)
    engine.say("Playing" + command)
    pywhatkit.playonyt(command)
    engine.runAndWait()

def time(command):
    engine.say("The time is" + datetime.datetime.now().strftime('%I:%M %p'))
    engine.runAndWait()


main()
