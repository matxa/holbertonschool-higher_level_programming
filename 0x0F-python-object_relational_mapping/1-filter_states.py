#!/usr/bin/python3
"""Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    connect_db = MySQLdb.connect(host="localhost", port=3066,
                                 user=argv[1], passwd=argv[2], db=argv[3])

    cursor_obj = connect_db.cursor()
    cursor_obj.execute(
        """SELECT * FROM states
        WHERE states.name LIKE 'N%'
        ORDER BY states.id ASC;""")

    query_rows = cursor_obj.fetchall()
    for row in query_rows:
        print(row)

    cursor_obj.close
    connect_db.close
