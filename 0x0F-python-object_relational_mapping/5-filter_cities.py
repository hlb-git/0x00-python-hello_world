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
    query = """SELECT c.name
            FROM cities as c
            INNER JOIN states as s
            ON c.state_id = s.id
            WHERE s.name=%s
            ORDER BY c.id ASC"""
    cur.execute(query, (args[4],))
    results = cur.fetchall()
    cities = [result[0] for result in results]
    for city in cities:
        print(city, end='')
        if city is not cities[len(cities) - 1]:
            print(', ', end='')
    print()
