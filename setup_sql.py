# import database
import sqlite3

# get connection/cusor
connection = sqlite3.connect('Account_infos.db')
cursor = connection.cursor()

print("connected to database successfully")

# creating a table
def create_table():
    sql_command_create = '''CREATE TABLE IF NOT EXISTS Accounts_infos(
    account_name VARCHAR(17),
    account_password VARCHAR(17),
    created DATE
    )'''
    cursor.execute(sql_command_create)
    connection.commit()

# inserting data into Accounts_infos table
def insert_data(username, password, created_date):
    sql_command_insert = 'INSERT INTO Accounts_infos(account_name, account_password, created) VALUES(?,?,?)'
    cursor.execute(sql_command_insert, (username, password, created_date))
    connection.commit()
