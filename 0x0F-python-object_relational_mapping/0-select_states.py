#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    """ at this point the script Takes command line arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """ Here the Connection to database is executed """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    """ Here a cursor is created for database """
    cursor = db.cursor()

    """ Execution of the SQL query Done """
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    """ Fetch all the rows in a list of lists """
    results = cursor.fetchall()

    """ Here's a command to Print the results """
    for row in results:
        print(row)

    """ Exit/Disconnect from the database """
    cursor.close()
    db.close()
