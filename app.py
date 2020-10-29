import msvcrt
import playsound

while True:
   if msvcrt.kbhit():
      key = msvcrt.getch()
      #print(key)   # just to show the result
      if (key == '\r'):
         playsound.playsound('./sound.mp3', True)
