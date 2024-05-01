#!/usr/bin/python3
"""
    connecting to MySQL database and
    execute your SQL queries.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    un = sys.argv[1]
    ps = sys.argv[2]
    d_b = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=un,
                           passwd=ps, db=d_b, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
