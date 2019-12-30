


import mysql.connector

mydb = mysql.connector.connect(
  host='localhost', port=3306, user='root', passwd='', db='camilo')

mycursor = mydb.cursor()

sql = "INSERT INTO compras (nombre,presio,cantidad) VALUES (%s, %s, %s)"
nombre = input("inserte el nombre: ")
presio = float(input("inserte el presio:"))
cantidad = int(input("inserte la cantidad"))


mycursor.execute(sql, (nombre,presio,cantidad))

mydb.commit()

print(mycursor.rowcount, "record inserted.")