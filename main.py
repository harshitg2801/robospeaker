'''
# for mac
import os

if __name__ == '__main__':
    print("Welcome to robospeaker 1.1 Created by Harshit Gupta")
    while True :
        x = input("Enter what you want me to speak : ")
        if x == "Bye" :
            break
        command = f"say {x}"
        os.system(command)
'''

#for windows
from gtts import gTTS
import os

mytext = input("Enter what you want me to speak : ")
# fh = open("test.txt", "r")
# mytext = fh.read().replace("\n" , " ")
language = 'en'
output = gTTS(text = mytext , lang = language , slow=False )

output.save("output.mp3")

#fh.close()

os.system("start output.mp3")