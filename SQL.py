import sqlite3

con = sqlite3.connect("packet.db")
cur = con.cursor()
cur.execute('SELECT * FROM sniff')
for row in cur:
    print row
con.commit()
cur.close()
