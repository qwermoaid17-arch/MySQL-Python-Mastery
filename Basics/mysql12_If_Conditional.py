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

        cr.execute("ALTER TABLE timee ADD COLUMN IF NOT EXISTS number INT(11)")

    def UPDATE(cr):

        cr.execute("UPDATE timee SET number = 24 WHERE id = 7")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 8")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 9")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 15")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 16")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 17")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 22")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 23")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 24")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 25")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 26")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 27")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 28")

        cr.execute("UPDATE timee SET number = 0 WHERE id = 29")

    def SELECT(cr):

        # cr.execute("SELECt id, name, IF(number  < 24, 'Hard Luck', 'Good') FROM timee")

        # cr.execute("SELECt id, name, IF(number  < 24, CONCAT('Hard Luck ', number), CONCAT('Good ', number)) FROM timee")

        cr.execute("SELECt id, name, IF(number  < 24, True, False) FROM timee")

        for row in cr.fetchall():

            print(row[0], row[1], row[2])


    def UPDATE(cr):

        cr.execute("UPDATE timee SET number = IF(number < 1 , + 10, number)")

    def SHOW(cr):

        cr.execute("SELECT * FROM timee")

        for row in cr.fetchall():

            print(row[0], row[1], row[2], row[3])

# Calling func:

    # INSERT(cr)

    # UPDATE(cr)

    SELECT(cr)

    # UPDATE(cr)

    # SHOW(cr) 

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()