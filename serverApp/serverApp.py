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

def userNameList():
    fulFireList = firebase.get('/profile/',None)
    return fulFireList.keys()









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

######################################################################################################


######################################## API operations area ##########################################


apikey = "AIzaSyBDR0vmhTIlG7UntsiN0MrUjSTDcwatB6Q"
cx = "003540993553648637127:x-4dcla6a9g"
googleurl = "https://www.googleapis.com/customsearch/v1"

def search(commonName):
    parameters = {"q":commonName,"cx":cx,"key":apikey}
    page = requests.request("GET", googleurl, params=parameters)
    results = json.loads(page.text)
    urlListofSearch = list()
    lengthofitems = len(results["items"])
    for numb in range(lengthofitems):
        urlset = results["items"][numb]["link"]
        urlListofSearch.append(urlset)
    return urlListofSearch




######################################################################################################


########################################## webscraping area of the project ################################

def scraper(url):
    page = requests.get(url)
    # html = urlopen(url)
    bsObj = BeautifulSoup(page.content,'html.parser')
    return str(bsObj.body)


######################################################################################################

######################################## analyser #######################################################



def mainAnnalyser(stng):
    countex = 0
    counth = 0
    countb = 0
    for badword in extremeList:
        if badword == None:
            continue
        else:
            countex = countex + stng.count(badword)
    for badword in highList:
        if badword == None:
            continue
        else:
            counth = counth + stng.count(badword)
    for badword in badList:
        if badword == None:
            continue
        else:
            countb = countb + stng.count(badword)
    fullcnt = (countex*10) + (counth*5) + countb
    howbad = (fullcnt/len(stng.split(" ")))*100
    return howbad



#################################################################################################################

######################################### All together <Major Code> ########################################################

def postResult(fullName,userName):
    searchList = search(fullName)
    for url in searchList:
        stng = scraper(url)
        howbadinweb = mainAnnalyser(stng)
        content={
            "url" : url,
            "howbad" : howbadinweb
        }
        firebase.post('/news/'+userName,content)

def doItForUser(username):
    userName = username
    fireUser = firebase.get('/profile/'+userName,None)
    userKeyDicList = fireUser.keys()
    keyValue = ""
    for i in userKeyDicList:
        keyValue = i
    fullName = firebase.get('/profile/'+userName+'/'+keyValue, 'fullName')
    postResult(fullName,userName)


def doItForAllUsers():
    getuserNameList = userNameList()
    for username in getuserNameList:
        doItForUser(username)
    print("done")

doItForAllUsers()


#################################################################################################################

######################################## button function area of the project ####################################

def startBtnAction():
    doItForAllUsers()

def stopBtnAction():
    print("stop button works well.....")

def addKeywordBtnAction():
    print("add keywords button works well.....")


######################################################################################################



######################################### interface Area of the project ##############################
''''
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
