from bs4 import BeautifulSoup
import urllib.request
import shutil
import requests
import os
import time
import sqlite3


def home():
    print("Work on this later")

def extractor(key, number):
        try: os.makedirs(r'C:\Comics\\' + key)
        except:
            None
        finally:
            i = 1
            url = requests.get('https://comiconlinefree.me/comic/' + str(key)).text
            soup = BeautifulSoup(url, 'html.parser')
            print(soup.prettify())
            
            
        
        
    



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
    if cursor.execute("SELECT * FROM comic WHERE key = \'" + keyword.lower() + "\' OR link = \'" + seriesLink + "\'").fetchall() != []:
        error("\nIt seems like that keyword or link is already in your library, maybe try again? \nx: Exit Program\nr: Restart Task\nh: Go Home\n\n", uploader)
    else:
        i = 0
        while i == 0:
            filling = input("\nIs it a FULL comic series?\nPlease enter y/n: ")
            if filling.lower() != 'y' and filling.lower() != 'n':
                print("\nI said to press y or n, can you read? Lets try again...")
            else:
                i = i + 1

        if filling.lower() == 'n':
            better = str("INSERT INTO comic VALUES(\'{}\', \'{}\', 0)")
            cursor.execute(better.format(keyword.lower(), seriesLink.replace("https://comiconlinefree.me/comic/", '')))
            con.commit()
        
        else:
            print("\nSince you are just uploading one file to the library, let's just download it right away!")




def downloader():
    akey = input("\nWhat is the Key for the comic you'd like to access? Or press h for help\n")
    if akey == 'h':
        home()#add list of all keys
    elif akey == 'x':
        None
    elif cursor.execute("SELECT * FROM comic WHERE key = \'" + akey.lower() + "\'").fetchall() == []:
        error("\nIt seems like that keyword isn't registered in your library, maybe try again? \nx: Exit Program\nr: Restart Task\nh: Go Home\n\n", downloader)
    else:
        amt = int(input("How many issues would you like to download?"))
        extractor(akey, 1)
         






    

intro = str(input("Welcome to Comicopy!! What would you like to do? \n \nd: download comics\np: post comic title to database\nr: remove a comic from library\n\n"))

if intro == "d":
    downloader()

elif intro == "p":
     uploader()

elif intro == "r":
    end = input("\nPlease enter the key of the comic you would like to remove from your library, enter h to go home, or x to exit this program:\n")
    if end == "h":
        home()
    elif end == "x":
        None
    else:
        cursor.execute("DELETE FROM comic WHERE key = \'" + end + "\'")
        con.commit()
        error("\nSuccesfully deleted " + end + ", if it even existed in the first place..\nr/h: home\nx: exit program ", home)



    
    


con.commit()
con.close() 