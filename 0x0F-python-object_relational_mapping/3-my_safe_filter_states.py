#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa \
where name matches the argument.

"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    search_name = argv[4]
    cur.execute("SELECT * FROM states WHERE name = '{}' \
                ORDER BY states.id".format(search_name))
    rows = cur.fetchall()

    for row in rows:
        if row[1] == search_name:
            print(row)
