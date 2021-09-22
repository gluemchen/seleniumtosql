# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
# )


# if mydb.connector(database="pythondb" not in mydb.connect):
#     mycursor = mydb.cursor()
#     mycursor.execute("CREATE DATABASE pythondb")
    
# # while check == True:
# #     for x in mycursor:

# for x in mycursor:
#     print(x)

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:5
    print(x)