"""Archivo temporal para la inserción de los datos en la base de datos"""
import pymysql
# import mysql.connector


# db = mysql.connector.connect("localhost","root","2010","pyconverter")
conexion = pymysql.connect(host="localhost",
                    user="root",
                    password="2010",
                    database="pyconverter")


# creando cursor
cursor = conexion.cursor()
instrucciones = "SHOW TABLES;"

cursor.execute(instrucciones)
filas = cursor.fetchall()

for fila in filas:
    print(fila)


# finalizar la base de datos
conexion.commit()
conexion.close()
