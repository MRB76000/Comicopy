import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
# cur.execute("""
#             INSERT INTO movie VALUES
#             ('Monty python and the holy grail', 1975, 8.2),('Iron Man', 2008, 10.0)""")
con.commit()
res = cur.execute("SELECT title FROM movie WHERE year = 2008")


print(res.fetchone())

con.commit() 
con.close() 