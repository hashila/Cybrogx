#all the imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import *
import json
import requests
import pandas as pd
from firebase import firebase
# from lib.google_search_results import GoogleSearchResults

# from search_google import api

#####firebase db connection

firebase = firebase.FirebaseApplication('https://cybrogx-1543512333299.firebaseio.com/', None)


########################################## firebase CRUD operations area #########################################
'''
def fullNameOfUser(username):
    userName = username
    fireUser = firebase.get('/profile/'+userName,None)
    userKeyDicList = fireUser.keys()
    keyValue = ""
    for i in userKeyDicList:
        keyValue = i
    fullName = firebase.get('/profile/'+userName+'/'+keyValue, 'fullName')
    return fullName # returns the full name of the given user name

def getFullNameList():
    userinfo = firebase.get('/profile/',None)
    keyList  = userinfo.keys()
    fullNameList = list()
    for k in keyList:
        ss = fullNameOfUser(k)
        fullNameList.append(ss)
    return fullNameList # this list use for the search api to search about the person on the internet

extremeList = firebase.get('/badWords/extreme',None) # list of extreme bad words
highList = firebase.get('/badWords/high',None) # list of high bad words
badList = firebase.get('/badWords/bad',None) # list of normal bad words




def sendExtreme():
    extreme ={

    }
    firebase.post('/badWords/extreme/',extreme)

def sendHigh():
    high = {

    }
    firebase.post('/badWords/high/',high)

def sendBad():
    bad = {

    }
    firebase.post('/badWords/bad/',bad)
'''
######################################################################################################


######################################## API operations area ##########################################


apikey = "AIzaSyBDR0vmhTIlG7UntsiN0MrUjSTDcwatB6Q"
cx = "003540993553648637127:x-4dcla6a9g"
googleurl = "https://www.googleapis.com/customsearch/v1"

parameters = {"q":"Mahinda","cx":cx,"key":apikey}
page = requests.request("GET", googleurl, params=parameters)
results = json.loads(page.text)

lengthofitems = len(results["items"])
for i in range(lengthofitems):
    print(results["items"][i]["link"])



######################################################################################################


########################################## webscraping area of the project ################################
'''
html = urlopen("https://www.javatpoint.com/")
bsObj = BeautifulSoup(html.read(),'html.parser')
print(bsObj.p)
'''
######################################################################################################


######################################## button function area of the project ####################################
'''
def startBtnAction():
    print("start button works well.....")

def stopBtnAction():
    print("stop button works well.....")

def addKeywordBtnAction():
    print("add keywords button works well.....")
'''

######################################################################################################



######################################### interface Area of the project ##############################
'''
root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

startbtn = Button(topFrame,text="Start",fg="white",bg="green",command=startBtnAction,height=5,width=20)
stopbtn = Button(topFrame,text="Stop",bg="red",fg="white",command=stopBtnAction,height=5,width=20)
addKeywordBtn = Button(bottomFrame,text="Add Keywords",bg="blue",fg="white",command=addKeywordBtnAction,height=5,width=20)

startbtn.pack()
stopbtn.pack()
addKeywordBtn.pack()


root.mainloop()
'''
######################################################################################################
