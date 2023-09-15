#!/usr/bin/python3
"""lists all states from the database"""
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
    query = "SELECT cities.id, cities.name , states.name FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)
    data = cursor.fetchall()
    for i in data:
        print(i)
    cursor.close()
    db.close()
