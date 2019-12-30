# aqui inportamos las librerias
import mysql.connector
import os

# aqui pide el nombre del usuario y lo guarda en una variable nombre
nombre=input("ingrese su nombre: \n ")
edad=int(input("ingrese su edad: \n"))
# aqui imprime la informacion que el usuario metio
print(f"su nombre es {nombre} y tienes {edad} años")
# aqui hacemos una condicion  if para que el usuario
# cumpla con el requisito de la edad minima para entrar
if edad < 12:
    print("no puede pasar por que eres muy joven")
else:
    print(f"bienvenido {nombre} \t")
def menu():
    os.system('cls')
    print("selecciona cualquiera de las siguientes opciones ")
    print("\t1 - primera opción  insertar datos ala base de datos")
    print("\t2 - segunda opción mostar datos")
    print("\t3 - tercera opción")
    print("\t9 - salir")
while True:
    menu()
    opcionmenu = input("ingrese una de las ociones ")
    if opcionmenu == "1":
        print("")
        import mysql.connector

        mydb = mysql.connector.connect(
            host='localhost', port=3306, user='root', passwd='', db='camilo')

        mycursor = mydb.cursor()

        sql = "INSERT INTO compras (nombre,presio,cantidad) VALUES (%s, %s, %s)"
        nombre = input("inserte el nombre: ")
        presio = float(input("inserte el presio:"))
        cantidad = int(input("inserte la cantidad"))

        mycursor.execute(sql, (nombre, presio, cantidad))

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        input("Has pulsado la opción 1...\npulsa una tecla para continuar")
    elif opcionmenu == "2":
        print("")
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
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    elif opcionmenu == "3":
        print("")
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionmenu == "9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")







