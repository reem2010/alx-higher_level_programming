#!/usr/bin/python3
from sys import argv
import MySQLdb
if __name__ == '__main__':
    host = "localhost"
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    port = 3306
    db = MySQLdb.connect(host, username, password, db_name, port)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    data = cursor.fetchall()
    for i in data:
        print(i)
    cursor.close()
    db.close()
