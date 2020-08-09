#!/usr/bin/python3
"""MySQLdb practice"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # connect to my sql server
    connect_db = MySQLdb.connect(host="localhost", port=3066, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])

    # making cursor obj for execution
    cur = connect_db.cursor()

    # executing
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    # fetch rows from cursor_obj
    query_rows = cur.fetchall()

    # loop through fetched rows
    for row in query_rows:
        print(row)

    # close cursor_obj and connect_db
    cur.close
    connect_db.close
