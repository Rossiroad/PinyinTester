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
while(learn == True):
    index = random.randint(0,49)
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
