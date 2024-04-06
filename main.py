from bs4 import BeautifulSoup
import urllib.request
import shutil
import os
import time
import sqlite3

def home():
    return "lol"

#establish db
con = sqlite3.connect("library.db")
cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE comic(key, link, lastIssue)")
    con.commit()

except:
    con.commit()

def error(message, current):
    ans = input(message)
    if ans.lower() == 'r':
        current()
    elif ans.lower() == 'h':
        home()
    elif ans.lower() == 'x':
        None
    else:
        error("\nYou did not provide a valid input, please press r, h or x\n\n", current=current)



    


def uploader():
    seriesLink = input("\nPlease paste the link of the comic series:\n")
    keyword = input("\nWhat would you like the keyword for this Series to be?\n")
    if cursor.execute("SELECT * FROM comic WHERE key = \'" + keyword + "\' OR link = \'" + seriesLink + "\'").fetchall() != []:
        error("\nIt seems like that keyword or link is already in your library, maybe try again? \nx: Exit Program\nr: Restart Task\nh: Go Home\n\n", uploader)
    else:
        better = str("INSERT INTO comic VALUES(\'{}\', \'{}\', 8)")
        cursor.execute(better.format(keyword, seriesLink))
        con.commit()



    

intro = str(input("Welcome to Comicopy!! What would you like to do? \n \nd: download comics\np: post comic title to database\nr: remove a comic from library\n\n"))

if intro == "d":
    #comic downloader
    title = input("What is the Keyword of the Comic you'd like to download?") #add a "press h for help" to display all keys

elif intro == "p":
     uploader()

elif intro == "r":
    end = input("\nPlease enter the key of the comic you would like to remove from your library, enter h to go home, or x to exit this program")
    if end == "h":
        home()
    elif end == "x":
        None
    else:
        cursor.execute("DELETE FROM comic WHERE key = \'" + end + "\'")
        con.commit()
        error("\nSuccesfully deleted " + end + ", if it even existed in the first place..\nr/h: home\nx: exit program ")



    
    


con.commit()
con.close() 