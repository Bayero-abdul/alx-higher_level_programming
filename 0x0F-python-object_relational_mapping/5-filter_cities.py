#!/usr/bin/python3
"""takes in the name of a state as an argument and
lists all cities of that state, using the db hbtn_0e_4_usa.

"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id=states.id \
                WHERE states.name = %s \
                ORDER BY cities.id", (argv[4],))
    rows = cur.fetchall()
    
    if rows:
        for i in range(len(rows)):
            if i == (len(rows) - 1):
                print(rows[i][0])
            else:
                print(rows[i][0], end=", ")
    else:
        print("")
