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

    def SHOW(cr):

        cr.execute("SELECT * FROM timee")

        for row in cr.fetchall():

            print(row[0], row[1], row[2])

    def in_and_not_in(cr):

        # cr.execute("SELECT * FROM timee WHERE id IN (8, 15 , 16)")

        # cr.execute("SELECT * FROM timee WHERE name IN (%s, %s)", ('mohab', 'None'))

        # cr.execute("SELECT * FROM timee WHERE id IN (%s, %s, %s, %s, %s, %s)", (8, 7, 9, 1, 15 , 11))

        # cr.execute("SELECT * FROM timee WHERE id NOT IN (%s, %s)", (8, 7))

        # cr.execute("SELECT * FROM timee WHERE date IN (%s, %s)", ('2026-5-22', '2024-6-10'))

        # cr.execute("SELECT * FROM timee WHERE REPLACE(date, '-', '/') IN (%s, %s)", ('2026-5-22', '2024-6-10'))


        cr.execute("SELECT * FROM timee WHERE date NOT IN (%s)", ('2026-5-22',))



        for row in cr.fetchall():

            print(row[0], row[1], row[2])


    # CALLING FUNC :

    in_and_not_in(cr)

    # SHOW(cr)

    

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()