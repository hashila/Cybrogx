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
'''
firebase = firebase.FirebaseApplication('https://cybrogx-1543512333299.firebaseio.com/', None)


########################################## firebase CRUD operations area #########################################

def userNameList():
    fulFireList = firebase.get('/profile/',None)
    return fulFireList.keys()



extremeList1 = firebase.get('/badWords/extreme',None) # list of extreme bad words
highList1 = firebase.get('/badWords/high',None) # list of high bad words
badList1 = firebase.get('/badWords/bad',None) # list of normal bad words

exx = extremeList1.keys()
hix = highList1.keys()
bax = badList1.keys()

extremeList = list()
highList = list()
badList = list()

for x in exx:
    f = firebase.get('/badWords/extreme',x)
    extremeList.append(f[1])
for x in hix:
    f = firebase.get('/badWords/high',x)
    highList.append(f[1])

for x in bax:
    f = firebase.get('/badWords/bad',x)
    badList.append(f[1])





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
    fullcnt = (countex*1000) + (counth*200) + countb
    howbad = (fullcnt/len(stng.split(" ")))*100
    return howbad



#################################################################################################################

######################################### All together <Major Code> ########################################################

def postResult(fullName,userName):
    searchList = search(fullName)
    for url in searchList:
        try:
            stng = scraper(url)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(e)
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
        try:
            doItForUser(username)
        except KeyError:
            print("key error")

    print("done")
'''
# doItForAllUsers()


#################################################################################################################
######################################## button function area of the project ####################################
def goback(window):#back function
    window.destroy()
    interfaceFunc()


def startBtnAction():
    # doItForAllUsers()
    print("start btn works well")

def stopBtnAction():
    print("stop button works well.....")

def addKeywordBtnAction(root):
    # global root
    root.destroy()

    window = Tk()


    T = Text(window, height=2, width=30)
    k = Text(window, height=2, width=30)
    n = Text(window, height=2, width=30)

    T.insert(END, "")
    k.insert(END, "")
    n.insert(END, "")

    hbtn = Button(window,text="highly bad word",fg="black",bg="yellow",command=lambda:sendHigh(k),height=1,width=20)
    exbtn = Button(window,text="Extremely bad word",bg="red",fg="black",command=lambda:sendExtreme(n),height=1,width=20)
    nbtn = Button(window,text="Normal bad word",bg="blue",fg="black",command=lambda:sendBad(T),height=1,width=20)
    backbtn = Button(window,text="BACK",bg="purple",fg="white",command=lambda:goback(window),height=1,width=20)

    T.pack()
    nbtn.pack(fill=X)
    k.pack()
    hbtn.pack(fill=X)
    n.pack()
    exbtn.pack(fill=X)
    backbtn.pack(fill=X)

    window.mainloop()

########################################################################################################################
################ send bad words ##########################


def sendExtreme(n):
    print("sendex")
    # input = n.get('1.0', END)
    # inputlist = input.split(",")
    #
    # for word in inputlist:
    #
    #     extreme ={
    #         "1" : word
    #     }
    #
    #     firebase.post('/badWords/extreme/',extreme)
    # n.delete('1.0', END)


def sendHigh(k):
    print("sendh")
    # input = k.get('1.0', END)
    # inputlist = input.split(",")
    # for word in inputlist:
    #
    #     high ={
    #         "1" : word
    #     }
    #
    #     firebase.post('/badWords/high/',high)
    # k.delete('1.0', END)


def sendBad(T):
    print("sendex")
    # input = T.get('1.0', END)
    # inputlist = input.split(",")
    #
    # for word in inputlist:
    #
    #     bad ={
    #         "1" : word
    #     }
    #
    #     firebase.post('/badWords/bad/',bad)
    # T.delete('1.0', END)

######################################################################################################
######################################### interface Area of the project ##############################


def interfaceFunc():
    root = Tk()

    topFrame = Frame(root)
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    startbtn = Button(topFrame,text="Start",fg="white",bg="green",command=startBtnAction,height=5,width=20)
    stopbtn = Button(topFrame,text="Stop",bg="red",fg="white",command=stopBtnAction,height=5,width=20)
    addKeywordBtn = Button(bottomFrame,text="Add Keywords",bg="blue",fg="white",command=lambda:addKeywordBtnAction(root),height=5,width=20)

    startbtn.pack()
    stopbtn.pack()
    addKeywordBtn.pack()


    root.mainloop()
######################################################################################################
######################################################################################################
######################################################################################################
interfaceFunc()      #init the app
######################################################################################################
######################################################################################################
######################################################################################################
