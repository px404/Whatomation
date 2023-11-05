#User checks are always important, uncomment the checks if you would like to enable them.

#The modules will be automatically installed once you run libs.py, if not, open cmd and run: pip install -r libs.txt

import os
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

print("\nWhatomation bot")

print("\nPlease ensure that WhatsApp web is logged in on the default browser before starting. (check settings to see the default)")

name = "contacts.csv"
contacts = str(input("\nHave you changed the name of the contacts file: contacts.csv? [1 = yes | 0 = no]: "))

if(contacts != "NO" or contacts != "No" or contacts != "no" or contacts != "n" or contacts!="0" or contacts!="2"):
    name = input("\n Enter the name of the file(without .csv - example: filename is: contact.csv > enter only contact(TEXT IS CASE SENSITIVE): ")
    name = name+".csv"
    print("The name entered is: ", name)

#input("\nPlease ensure that the program is in the same folder as "+name+", if it is, press enter, if it isn't then combine them and restart the program.") #User check - always assume the user will mess with something

input("\nPlease don't move the cursor or use the pc while the program is running as it can interfere with the bot.\nPress enter to continue.")
time.sleep(5)

try:
    data = pd.read_csv(name)
    try:
        print("\nParsing the data")
        data_dict = data.to_dict('list')
        number = data_dict['PhoneNum']
        text = data_dict['Text']
        combo = zip(number,text)

        try:
            for number,text in combo:
                print("\nOpening WhatsApp to send the text: "+text+" to: "+str(number))
                web.open("https://web.whatsapp.com/send?phone="+str(number)+"&text="+text)
                try:
                    time.sleep(7)
                    width,height = pg.size()
                    pg.click(width/2,height/2)
                    try:
                        time.sleep(7)
                        pg.press('enter')
                        time.sleep(7)
                        pg.hotkey('ctrl', 'w')
                    except:
                        print("\nError while sending message to: "+str(number)+" likely caused due to insufficient click of the mouse or moving the mouse or using it.")
                except:
                    print("\nError while sending message to: "+str(number)+". The text was "+text)
            
        except:
            print("\Error in sending all messages.")
    except:
        print("\nThere is an error in data parsing.")

except:
    print("\n"+name+" doesn't exist.")
