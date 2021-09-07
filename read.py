import sqlite3

cnt = sqlite3.connect('topics.db')
result= cnt.execute('SELECT * FROM topic')
abc = result.fetchall()
for a in abc:
    print(a)