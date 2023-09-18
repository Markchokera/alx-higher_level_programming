#!/usr/bin/python3
"""lists all the states from the database htbn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        database_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = database_connection.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        results = cursor.fetchall()
        for result in results:
            print(result)
        database_connection.close()
