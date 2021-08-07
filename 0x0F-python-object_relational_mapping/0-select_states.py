
if __name__ == "__main__":
    import MySQLdb as my
    from sys import argv

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = my.connect(host="localhost", user=username,
                    passwd=password, db=db_name)
    db.query("""SELECT * FROM states ORDER BY states.id ASC;""")
    rows = db.store_result()
    for row in rows.fetch_row(0):
        print(row)
