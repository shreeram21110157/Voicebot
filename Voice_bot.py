## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS
import pyttsx3
from tkinter import *
def redirector(inputStr):
    output.insert(INSERT, inputStr)


def click():
    sr.energy_threshold = 3000
    sr.pause_threshold = 0.3
    
    # sender = input("What is your name?\n")
    
    
    
    bot_message = ""
    message=""
    
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})
    
    print("Bot says, ",end=' ')
   
    
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")
        
    
    
    while bot_message != "Bye" or bot_message!='thanks':
    
        r = sr.Recognizer()  # initialize recognizer
        with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
            print("Speak Anything :")
            
            audio = r.listen(source)  # listen to the source
            try:
                message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
                print("You said : {}".format(message))
                
    
            except:
                print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
                
        if len(message)==0:
            continue
        print("Sending message now...")
        
    
        r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
    
        print("Bot says, ",end=' ')
        
        for i in r.json():
            bot_message = i['text']
            eng = pyttsx3.init()
            eng.say(i['text'])
            eng.runAndWait()
            print(f"{bot_message}")
            
    
        
        
        if bot_message.lower()=='bye':
            break
        
    
window = Tk()
window.title("Voice Assisstant MiniProject")
window.configure(background="black")
#Create Label
Label (window, text="Click to start the assistant",bg="black",fg="white",font="none 12 bold") .grid(row=1, column=0, sticky=W)

Button (window, text="START", width=6, command=click) .grid(row=3, column=0, sticky=W)
Label (window, text="\nOutput:",bg="black", fg="white", font="Helvetica") .grid(row=4, column=0, sticky=W)
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

window.mainloop()   
