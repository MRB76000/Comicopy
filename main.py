#fresh start
from bs4 import BeautifulSoup
import urllib.request
import shutil
import os
import time
import json




intro = str(input("Welcome to Comicopy!! What would you like to do? \n \nd: download comics\np: post comic title to database\n\n:"))

if intro == "d":
    #comic downloader
    None
elif intro == "p":
    #comic uploader
    seriesLink = input("Please paste the link of the comic series/an issue of it:\n")
    keyword = input("\nWhat would you like they keyword for this Series to be?\n")
    fake = {
        keyword: seriesLink
    }
    z = open("db.json").read()
    open("db.json", 'w').write(str(z).replace("}", ",\n") + json.dumps(fake).replace("{", ""))
    
    



