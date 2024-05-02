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
    state = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                           passwd=db_ps, db=db_name, charset="utf8")
    cur = conn.cursor()
    sql = f"SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    try:
        cur.execute(sql, (state,))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except Exception as e:
        print("Error:", e)

    finally:
        cur.close()
        conn.close()
