#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state))

    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
