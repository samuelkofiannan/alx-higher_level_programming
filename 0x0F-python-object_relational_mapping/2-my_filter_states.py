#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv


def lists_states(user, password, database, search_query):
    """Lists states in the database"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    query = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(search_query)
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    lists_states(argv[1], argv[2], argv[3], argv[4])
