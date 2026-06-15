import pymysql as sql 

import pymysql as sql 

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("USE tests")

    def INSERT(cr):

        # cr.execute("INSERT INTO timee (name, date) VALUES ('yed', '2022-02-02')")

        # cr.execute("INSERT INTO timee (name, date) VALUES (%s, %s)", ('oha', '2022-02-02'))

        # cr.execute("INSERT INTO timee (name, date) VALUES (%s, %s)", ('AAA', '2022-02-02'))

        # cr.execute("INSERT INTO timee (name, date) VALUES (%s, %s)", ('m%d', '2022-02-02'))

        cr.execute("INSERT INTO timee (name, date) VALUES (%s, %s)", ('moheb', '2022-02-02'))

    def SHOW(cr):

        cr.execute("SELECT * FROM timee")

        for row in cr.fetchall():

            print(row[0], row[1], row[2])

    def like_percent(cr):

        # cr.execute("SELECT * FROM timee WHERE name LIKE 'maoyed'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE 'aoyed'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%aoyed'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%yed'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%oha%'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%y%'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%m%'")

        # cr.execute("SELECT * FROM timee WHERE name not LIKE '%m%'")

        # cr.execute("SELECT * FROM timee WHERE name  LIKE 'm%d'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%o%a%'")

        cr.execute("SELECT * FROM timee WHERE name LIKE '%a%a%'")


        for row in cr.fetchall():

            print(row[0], row[1], row[2])


    def like_underscore(cr):

        # cr.execute("SELECT * FROM timee WHERE name LIKE '_yed'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '___yed'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '_aoyed'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE 'moh_b'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%moh_b'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%h_b'")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%_b'")

        cr.execute("SELECT * FROM timee WHERE name LIKE '%_%'")


        for row in cr.fetchall():

            print(row[0], row[1], row[2])

    def Not_like(cr):

        cr.execute("SELECT * FROM timee WHERE name not LIKE 'moh_b'")

        for row in cr.fetchall():

            print(row[0], row[1], row[2])


    # CALLING FUNC :

    # INSERT(cr)

    # like_percent(cr)

    # like_underscore(cr)

    Not_like(cr)

    # SHOW(cr)

    

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()