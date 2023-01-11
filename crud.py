import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='bdSales',
)

cursor = connection.cursor()

#CRUD aqui

cursor.close()
connection.close()