import sqlite3
con = sqlite3.connect("demo.db")
cur = con.cursor()
# cur.execute("CREATE TABLE comic(key, link, last page)")
# cur.execute("""
#             INSERT INTO comic VALUES
#             ('USM', 'ultimate spiderman.com', 8),('Iron Man', 'im.com', 10)""")
# con.commit()
# res = cur.execute("SELECT link FROM comic WHERE key = 'USM'")

cur.execute("DELETE FROM comic WHERE key = 'Iron Man'")


# print(str(res.fetchone()).replace('(','').replace(')', '').replace(',', '').replace('\'', '').replace(',', ''))

con.commit() 
con.close() 