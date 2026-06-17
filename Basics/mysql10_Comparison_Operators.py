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

    def SELECT_Comparison_Operators(cr):

        # =

        # cr.execute("SELECT * FROM timee WHERE id = 8")

        # >

        # cr.execute("SELECT * FROM timee WHERE id > 8")

        # >=

        # cr.execute("SELECT * FROM timee WHERE id >= 8")

        # <

        # cr.execute("SELECT * FROM timee WHERE id < 18")

        # <=

        # cr.execute("SELECT * FROM timee WHERE id <= 18")

        # !=

        # cr.execute("SELECT * FROM timee WHERE id != 8")

        # ANOTHER WAY

        cr.execute("SELECT * FROM timee WHERE id <> 8")

        for row in cr.fetchall():

            print(row[0], row[1], row[2])

    def DELTE(cr):

        cr.execute("DELETE FROM timee WHERE name IS NULL") 

    # CALLING FUNC :

    # DELTE(cr)

    # SHOW(cr)

    SELECT_Comparison_Operators(cr)



    

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()