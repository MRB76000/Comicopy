from bs4 import BeautifulSoup
import urllib.request
import shutil
import requests
import os
import time
import sqlite3
from PIL import Image


def home():
    print("Work on this later")

def extractor(key, number):
    pages = []
    issue = number
    dirName = r'/home/mason/comics/' + key
    os.makedirs(r'/home/mason/comics/junk')
    try: os.makedirs(dirName)
    except:
        None
    finally:
        i = 1
        url = requests.get('https://comiconlinefree.me/' + str(key) + "/issue-" + str(issue) + "/full").text
        soup = BeautifulSoup(url, 'html.parser')
        for page in soup.find_all("img", {"class": "lazyload chapter_img"}):
            start = (str(page).index("https"))
            end = (str(page).find("\"", start + 1))
            number = str(page).index("Page ")
            try:
                int(str(page)[number + 6]) / 2
                second = str(page)[number + 6]
                try:
                    int(str(page)[number + 7]) / 2
                    third = str(page)[number + 7]
                    pn = str(page)[number + 5] + second + third
                except:
                    pn = str(page)[number + 5] + second 
            except:
                pn = str(page)[number + 5]
            pages.append("page " + pn + ".jpg")
            imageLink = str(page)[start:end] 
            urllib.request.urlretrieve(imageLink, "page " + pn + ".jpg")
            shutil.move("/home/mason/vscode projects/Python-Comic-Downloader/page " + pn + ".jpg", "/home/mason/comics/junk")
            print(pn)
        images = [
            Image.open("/home/mason/comics/junk" +'/' + f)
            for f in pages]
        pdf_path = dirName + '/issue ' + str(issue) + ".pdf"
        images[0].save(
            pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
        path = os.path.join("/home/mason/comics/", "junk") #might draw an eror for /
        shutil.rmtree(path)


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
    elif cursor.execute("SELECT * FROM comic WHERE key = \'" + akey + "\'").fetchall() == []:
        error("\nIt seems like that keyword isn't registered in your library, maybe try again? \nx: Exit Program\nr: Restart Task\nh: Go Home\n\n", downloader)
    else:
        amt = int(input("How many issues would you like to download?"))
        keyoto = cursor.execute("SELECT link FROM comic WHERE key = \'" + akey + "\'").fetchall() #link
        numb = cursor.execute("SELECT lastIssue FROM comic WHERE key = \'" + akey + "\'").fetchall() #las issue
        nomper = len(str(keyoto)) #lenght of the link
        new = str(keyoto)[3:nomper - 4]
        extractor(new, 1)

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