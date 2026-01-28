import mysql.connector

def db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Helia183@",
        database="foodshop1"
    )
