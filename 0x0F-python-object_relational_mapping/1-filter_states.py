#!/usr/bin/python3
"""
    connecting to MySQL database and
    execute your SQL queries.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db_user = sys.argv[1]
    db_ps = sys.argv[2]
    db_name = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                           passwd=db_ps, db=db_name, charset="utf8")
    cur = conn.cursor()
    sql = "SELECT * FROM states WHERE UPPER(name) LIKE 'N%' ORDER BY id ASC"
    try:
        cur.execute(sql)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except Exception as e:
        print("Error:", e)

    finally:
        cur.close()
        conn.close()
