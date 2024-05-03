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
    sql = """
    SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    try:
        cur.execute(sql, (state,))
        query_rows = cur.fetchall()
        city_names = [city[0] for city in query_rows]
        formatted_output = ", ".join(city_names)
        print(formatted_output)
    except Exception as e:
        print("Error:", e)

    finally:
        cur.close()
        conn.close()
