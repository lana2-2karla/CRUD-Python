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

#read

command = f'SELECT * FROM Sales'
cursor.execute(command)
result = cursor.fetchall() #captura dados do BD
print(result) # Tupla [(1, 'toddynho', 4), (2, 'nescau', 3)]




cursor.close()
connection.close()