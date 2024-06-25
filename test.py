# import sqlite3
# con = sqlite3.connect("library.db")
# cur = con.cursor()
# # cur.execute("CREATE TABLE comic(key, link, last page)")
# # cur.execute("""
# #             INSERT INTO comic VALUES
# #             ('USM', 'ultimate spiderman.com', 8),('Iron Man', 'im.com', 10)""")
# # con.commit()
# # res = cur.execute("SELECT link FROM comic WHERE key = 'k'")

# cur.execute("DELETE FROM comic WHERE key = 'k'")
# # keyword ="key"
# # print(cur.execute("SELECT * FROM comic WHERE key = \'" + keyword + "\'").fetchall())

# # print(str(res.fetchone()).replace('(','').replace(')', '').replace(',', '').replace('\'', '').replace(',', ''))

# con.commit() 
# con.close() 



# balls = "real"
# print(balls.replace("hweqiowqh",''))


from numpy import kaiser
import requests
import urllib.request
from bs4 import BeautifulSoup

import shutil
import os
import time

# urllib.request.urlretrieve("https://2.bp.blogspot.com/-duVlikrjQM0/VnkHCAYI-SI/AAAAAAAADbE/Uipvnewo3P8/s0-Ic42/RCO001.jpg", "page" + "5" + ".jpg")


key = "moon-knight-1980"
number = 1
dirName = r'/home/mason/comics/' + key
try: os.makedirs(dirName)
except:
    None
finally:
    i = 1
    url = requests.get('https://comiconlinefree.me/' + str(key) + "/issue-" + str(number) + "/full").text
    soup = BeautifulSoup(url, 'html.parser')



    #this was copied

    for page in soup.find_all("img", {"class": "lazyload chapter_img"}):
        
        start = (str(page).index("https"))
        end = (str(page).index(".jpg"))

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

        imageLink = str(page)[start:end] + ".jpg"
        urllib.request.urlretrieve(imageLink, "page " + pn + ".jpg")
        shutil.move("/home/mason/vscode projects/Python-Comic-Downloader/page " + pn + ".jpg", dirName)
        print(pn)


# url = requests.get("https://comiconlinefree.me/moon-knight-1980/issue-1/full")

# print(url.text)


# session = HTMLSession()
# r = session.get('https://comiconlinefree.me/moon-knight-1980/issue-1')

# r.html.render()


# print(r.html.html)
# soup = BeautifulSoup(r.html.html, 'html.parser')


# rally = soup.find_all('img')

# print(rally)



