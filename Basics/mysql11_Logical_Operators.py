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

    def LOGICAL_AND(cr):

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%ohamed' AND id > 10")

        cr.execute("SELECT * FROM timee WHERE name LIKE '%ohamed' AND id < 10")


        for row in cr.fetchall():

            print(row[0], row[1], row[2])

    def LOGICAL_NOT(cr):

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%ohamed' AND NOT id > 10")

        cr.execute("SELECT * FROM timee WHERE NOt name LIKE '%ohamed' AND NOT id < 10")

        for row in cr.fetchall():

            print(row[0], row[1], row[2])

    def logical_OR(cr):

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%ohamed' OR id > 100")

        cr.execute("SELECT * FROM timee WHERE name LIKE '%ohamed' OR id > 10")

        for row in cr.fetchall():

            print(row[0], row[1], row[2])

    def Logical_XOR(cr):

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%ohamed' XOR id > 100")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%ohamed' XOR id < 10")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%ohamygffuied' XOR id > 1000")

        # cr.execute("SELECT * FROM timee WHERE name LIKE '%ofjamed' XOR id > 10")

        cr.execute("SELECT * FROM timee WHERE name LIKE '%ofjamed' XOR id <= 10")


        for row in cr.fetchall():

            print(row[0], row[1], row[2])

    # CALLING FUNC :

    # LOGICAL_AND(cr)

    # LOGICAL_NOT(cr)

    # logical_OR(cr)

    Logical_XOR(cr)

    # SHOW(cr)



    

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()