# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="192.168.0.7",
#   user="root",
#   password="1"
# )

import sqlite3

mydb = sqlite3.connect('../db.sqlite3')