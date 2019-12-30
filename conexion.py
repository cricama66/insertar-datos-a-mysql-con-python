import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='camilo')



cur = conn.cursor()
cur.execute("SELECT * FROM compras")

print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()

