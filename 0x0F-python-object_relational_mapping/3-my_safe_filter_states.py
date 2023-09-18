#!/usr/bin/python3
"""takes an argument and displays values in the
states table of htbn_0e_usa where name matches the
argument, safe from SQL injections"""

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) >= 5:
        database_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        state_name = sys.argv[4]
        cursor = database_connection.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE %s " +
            "ORDER BY id ASC", [state_name]
        )
        results = cursor.fetchall()
        for result in results:
            print(result)
        database_connection.close()
