import sqlite3
cnn = sqlite3.connect('testDB.db')
cur = cnn.cursor()
cur.execute('select * from table1')
print(cur.fetchall())
cnn.close()
