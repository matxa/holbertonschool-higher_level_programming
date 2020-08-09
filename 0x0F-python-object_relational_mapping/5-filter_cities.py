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
    cursor_obj.execute(
        """SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %(state)s;""",
        {'state': argv[4]})

    # fetch rows from cursor_obj
    query_rows = cursor_obj.fetchall()

    # loop through fetched rows
    for i in range(len(query_rows)):
        print(query_rows[i][0], end="")
        if i != len(query_rows) - 1:
            print(", ", end="")
    print()

    # close cursor_obj and connect_db
    cursor_obj.close
    connect_db.close
