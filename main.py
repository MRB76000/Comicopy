from bs4 import BeautifulSoup
import urllib.request
import shutil
import requests
import os
import time
import sqlite3
<<<<<<< HEAD

from file_getter import pop
=======
#github sucks
from PIL import Image


>>>>>>> b45bcae0282b652e2ebdad16a8501d17342c4c47

def home():
    print("Work on this later")

def extractor(key, number):
<<<<<<< HEAD
        try: os.makedirs(r'C:\Comics\\' + key)
        except:
            None
        finally:
            i = 1
            url = requests.get('https://comiconlinefree.me/' + str(key) + "/issue-" + str(number) + "/full").text
            soup = BeautifulSoup(url, 'html.parser')
            print(soup.prettify())


            
            
            
        
        
    



#establish db
=======
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


>>>>>>> b45bcae0282b652e2ebdad16a8501d17342c4c47
con = sqlite3.connect("library.db")
cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE comic(key, link, lastIssue)")
    con.commit()
<<<<<<< HEAD

except:
    con.commit()

=======
except:
    con.commit()
>>>>>>> b45bcae0282b652e2ebdad16a8501d17342c4c47
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
<<<<<<< HEAD


=======
>>>>>>> b45bcae0282b652e2ebdad16a8501d17342c4c47
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
<<<<<<< HEAD

=======
>>>>>>> b45bcae0282b652e2ebdad16a8501d17342c4c47
        if filling.lower() == 'n':
            better = str("INSERT INTO comic VALUES(\'{}\', \'{}\', 0)")
            cursor.execute(better.format(keyword.lower(), seriesLink.replace("https://comiconlinefree.me/comic/", '')))
            con.commit()
<<<<<<< HEAD
        
=======
>>>>>>> b45bcae0282b652e2ebdad16a8501d17342c4c47
        else:
            print("\nSince you are just uploading one file to the library, let's just download it right away!")


<<<<<<< HEAD


=======
>>>>>>> b45bcae0282b652e2ebdad16a8501d17342c4c47
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
<<<<<<< HEAD
        keyoto = cursor.execute("SELECT link FROM comic WHERE key = \'" + akey + "\'").fetchall()
        numb = cursor.execute("SELECT lastIssue FROM comic WHERE key = \'" + akey + "\'").fetchall()
        nomper = len(str(keyoto))
        new = str(keyoto)[3:nomper - 4]
        extractor(new, 1)
         






    

intro = str(input("Welcome to Comicopy!! What would you like to do? \n \nd: download comics\np: post comic title to database\nr: remove a comic from library\n\n"))

if intro == "d":
    downloader()

elif intro == "p":
     uploader()

=======
        keyoto = cursor.execute("SELECT link FROM comic WHERE key = \'" + akey + "\'").fetchall() #link
        numb = str(cursor.execute("SELECT lastIssue FROM comic WHERE key = \'" + akey + "\'").fetchall()).replace('[(','').replace(',)]', '')
        print(numb)
        nomper = len(str(keyoto)) #lenght of the link
        new = str(keyoto)[3:nomper - 4]
        for k in range(amt):
            extractor(new, int(k) + 1 + int(numb))
        cursor.execute(f"UPDATE comic SET lastIssue = {int(numb) + amt} WHERE key = \'moon1980\'")
        #cursor.execute('''UPDATE EMPLOYEE SET INCOME = 5000 WHERE Age<25;''') 
        

intro = str(input("Welcome to Comicopy!! What would you like to do? \n \nd: download comics\np: post comic title to database\nr: remove a comic from library\n\n"))
if intro == "d":
    downloader()
elif intro == "p":
     uploader()
>>>>>>> b45bcae0282b652e2ebdad16a8501d17342c4c47
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
<<<<<<< HEAD



    
    


=======
>>>>>>> b45bcae0282b652e2ebdad16a8501d17342c4c47
con.commit()
con.close() 