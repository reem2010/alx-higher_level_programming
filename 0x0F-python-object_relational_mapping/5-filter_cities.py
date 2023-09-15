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
    query = "SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')FROM cities \
            WHERE cities.state_id = (SELECT states.id \
            FROM states WHERE states.name LIKE BINARY %s LIMIT 1) \
            "
    cursor.execute(query, (argv[4],))
    data = cursor.fetchall()
    for i in data:
        print(i[0])
    cursor.close()
    db.close()
