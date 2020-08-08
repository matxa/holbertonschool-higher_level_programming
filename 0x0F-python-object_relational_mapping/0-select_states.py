#!/usr/bin/python3
"""MySQLdb practice"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # connect to my sql server
    connect_db = MySQLdb.connect(host="localhost", port=3066, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])

    # making cursor obj for execution
    cursor_obj = connect_db.cursor()

    # executing
    cursor_obj.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # fetch rows from cursor_obj
    query_rows = cursor_obj.fetchall()

    # loop through fetched rows
    for row in query_rows:
        print(row)

    # close cursor_obj and connect_db
    cursor_obj.close
    connect_db.close

