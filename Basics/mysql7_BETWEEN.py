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

    def INSET(cr):

        cr.execute("INSERT INTO timee (date) VALUES  (%s)", ('2026-5-20',))

        cr.execute("INSERT INTO timee (date) VALUES  (%s)", ('2026-5-22',))

    def SELECT_BETWEEN(cr):

        # cr.execute("SELECT * FROM timee WHERE id BETWEEN 8 AND 8999 ")

        # cr.execute("SELECT * FROM timee WHERE date BETWEEN '2026-5-16' AND '2026-5-25'")

        # cr.execute("SELECT * FROM timee WHERE date BETWEEN '2026-5-5' AND '2026-5-17'")

        # cr.execute("SELECT * FROM timee WHERE date BETWEEN '2026-5-5' AND '2029-5-17' ORDER BY date ")

        # cr.execute("SELECT * FROM timee WHERE date BETWEEN date_SUB(CURDATE(), INTERVAL 2 MONTH) AND CURDATE()")

        # cr.execute("SELECT * FROM timee WHERE date BETWEEN date_SUB(CURDATE(), INTERVAL 1 year) AND CURDATE()")

        # cr.execute("SELECT * FROM timee WHERE date NOT BETWEEN date_SUB(CURDATE(), INTERVAL 1 year) AND CURDATE()")

        # cr.execute("SELECT * FROM timee WHERE date BETWEEN date_SUB(CURDATE(), INTERVAL 10 DAY) AND CURDATE()")

        # cr.execute("SELECT * FROM timee WHERE date BETWEEN date_SUB('2026-5-28', INTERVAL 10 DAY) AND '2026-5-28'")

        cr.execute("SELECT * FROM timee WHERE date NOT BETWEEN date_SUB('2026-5-28', INTERVAL 10 DAY) AND '2026-5-28'")










        for row in cr.fetchall():

            print(row[0], row[1], row[2])

    # CALLING FUNC :

    # INSET(cr)

    SELECT_BETWEEN(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()