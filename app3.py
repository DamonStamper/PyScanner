import os
import playsound
import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)
engine.setProperty('rate', 125) 

while True:
    keys = input("Scan a barcode right now:")
    if keys == "016500508274":
        print("Bactine")
        engine.say('Bactine')
        engine.runAndWait()
    if keys == "01324671":
        print("Pills")
        engine.say('Pills')
        engine.runAndWait()
    #if (key == b'\r' or key == b'\n' or key == b'\r\n' or key == b'\n\r'):        
    #print(key)   # just to show the result
    else:
        playsound.playsound('./sound.mp3', True)