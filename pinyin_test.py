import pinyin
import random
import binascii
#import pyttsx3
# coding: utf8

#engine = pyttsx3.init()
file = open('frequency.txt','r', encoding='utf8')
lines = file.read()
hanzi = lines.split('\n')
length = len(hanzi) - 1
learn = True
reviews = 0
removed = 0
while(learn == True):
    index = random.randint(10,99)
    word = hanzi[index]
    print(word)
    again = input()
    #engine.say(word)
    #engine.runAndWait()
    print(pinyin.get(word))
    reviews += 1
    print("Reviews:" + str(reviews))
    if(again == "r"):
        check = input("Are you sure you want to delete this? ((y/r)/n)")
        if(check == "y" or check == "r"):
            del hanzi[index]
            length = length - 1
            removed += 1
    elif (again == "stop"):
        break

print("Congratuations on finishing your session!")
print("You studied " + str(reviews) + " words in total!")
print("You removed " + str(removed) + " words in total!")
