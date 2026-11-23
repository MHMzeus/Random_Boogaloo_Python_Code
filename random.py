from time import sleep
from random import randint
import re

#Third layer
Day = 'I am doing quite well thanks for asking. Do you know what day it is today?'
Number = randint(1, 31)
def ran(Number, Day):
    print(Day)
    Month = input('Type in one of the twelve months from the year: ').capitalize()
    print("Yes, it is" , Month, str(Number) + ".")
    Year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    Y2 = Year[-1:] + Year[:2]
    if Month[:3] in Y2:
        print("Its one of three months in the winter season.")
    elif Month[:3] in Year[2:5]:
        print("Its one of three months in the spring season.")
    elif Month[:3] in Year[5:8]:
        print("Its one of three months in the summer season.")
    elif Month[:3] in Year[8:11]:
        print("Its one of three months in the autumn season.")
    else:
        print("Did not match with the elements in the", len(Year), "list.")
#--- 


#Second layer
Fluff = ['On this fine day?', 'On this horrendous day?', 'On this mediocre day?']
def day(Fluff):
    E_N = input('Type in a number between 0-2: ')
    if re.search('[0]{1}', E_N):
        print(Fluff[0])
        ran(Number, Day)
    elif re.search('[1]{1}', E_N):
        print(Fluff[1])
        ran(Number, Day)
    elif re.search('[2]{1}', E_N):
        print(Fluff[2])
        ran(Number, Day)
    else:
        print("The given number did not align with the function.")
#---



#First layer
U_i = None
Tries = 0
Greeting = ['Hi,', 'Hello,', 'Greetings,']
Questioning = ' How are you doing.'
#---

while U_i != 'Hi' or U_i != 'Hello' or U_i != 'Greetings' and Tries < 3:
    U_i = input('Type in either hi, hello or greetings: ').capitalize() + ','
    if U_i in Greeting[0]:
       print(Greeting[0] + Questioning)
       day(Fluff)
       break
    elif U_i in Greeting[1]:
       print(Greeting[1] + Questioning)
       day(Fluff)
       break
    elif U_i in Greeting[2]:
       print(Greeting[2] + Questioning)
       day(Fluff)
       break
    elif Tries == 3:
        Tries -= 3
        print("The blessed code required a cooldown, give it 5 seconds.")
        sleep(1)
        print(1)
        sleep(1)
        print(2)
        sleep(1)
        print(3)
        sleep(1)
        print(4)
        sleep(1)
        print(5)
    else:
       print("I required a " + str(Greeting) + " to be typed in which clearly did not occur, try again!")
       Tries += 1
       sleep(1)
       print(1)
       sleep(1)
       print(2)
       sleep(1)
       print(3)
