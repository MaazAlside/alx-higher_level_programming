#!/usr/bin/python3
""" Script all values in the states table of hbtn_0e_0_usa """
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
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (state,))

    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
