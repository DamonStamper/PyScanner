import msvcrt
import playsound

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        #print(key)   # just to show the result
        if (key == b'\r' or key == b'\n' or key == b'\r\n' or key == b'\n\r'):
            playsound.playsound('./sound.mp3', True)
            print(key)