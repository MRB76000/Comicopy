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


import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession




url = requests.get("https://comiconlinefree.me/moon-knight-1980/issue-1/full")

print(url.text)


# session = HTMLSession()
# r = session.get('https://comiconlinefree.me/moon-knight-1980/issue-1')

# r.html.render()


# print(r.html.html)
# soup = BeautifulSoup(r.html.html, 'html.parser')


# rally = soup.find_all('img')

# print(rally)



