import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='bdSales',
)

cursor = connection.cursor()

#CRUD

name_product = 'toddynho'
value = 4

#Create

command = f'INSERT INTO Sales (product_name, value) VALUES ("{name_product}", {value})'
cursor.execute(command)
connection.commit() #edita banco de dados

cursor.close()
connection.close()