#!/usr/bin/python3
"""selects rows in a table"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv
    if (len(args) != 5):
        raise Exception('need 3 arguments')

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=args[1],
                           passwd=args[2],
                           db=args[3])

    cur = conn.cursor()
    query = """SELECT * FROM states WHERE name=%s
            ORDER BY id ASC"""
    cur.execute(query, (args[4],))
    results = cur.fetchall()
    for row in results:
        print(row)
