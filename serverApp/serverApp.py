#all the imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import *
import json
import requests
import pandas as pd
import pyrebase
'''
#firebase db connection
config = {
    apiKey: "AIzaSyB-0Zcia1IrqEzMn39qp-JrEaGeoON57-Y",
    authDomain: "cybrogx-1543512333299.firebaseapp.com",
    databaseURL: "https://cybrogx-1543512333299.firebaseio.com",
    projectId: "cybrogx-1543512333299",
    storageBucket: "cybrogx-1543512333299.appspot.com",
    messagingSenderId: "1048992728209"
  }
rebase = pyrebase.initialize_app(config)


#API operations area
apikey = "AIzaSyBDR0vmhTIlG7UntsiN0MrUjSTDcwatB6Q"
cx = "003540993553648637127:x-4dcla6a9g"

url = "https://www.googleapis.com/customsearch/v1"
parameters = {"q":"Damith","cx":cx,"key":apikey}
page = requests.request("GET", url, params=parameters)
results = json.loads(page.text)
print(results["items"])




#webscraping area of the project
# html = urlopen("https://www.javatpoint.com/")
# bsObj = BeautifulSoup(html,'lxml')
# print(bsObj.h1)



#button function area of the project

def startBtnAction():
    print("start button works well.....")

def stopBtnAction():
    print("stop button works well.....")

def addKeywordBtnAction():
    print("add keywords button works well.....")





#interface Area of the project
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
