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

    def UPDATE(cr):


        cr.execute("UPDATE timee SET number = 15 WHERE id = 22")

        cr.execute("UPDATE timee SET number = 15 WHERE id = 23")

        cr.execute("UPDATE timee SET number = 15 WHERE id = 24")

    def SELECT(cr):

        # cr.execute("SELECT id, name, CASE WHEN number = 10 THEN 'NOT BAD' " \
        # "WHEN number = 15 THEN 'GOOD' " \
        # "WHEN number = 24 THEN 'Perfect' " \
        # "ELSE 'UNKNOWN' END as result " \
        # "FROM timee")


        # cr.execute("SELECT id, name, CASE WHEN number > 10 THEN 'GOOD' " \
        # "WHEN number = 24 THEN 'Perfect' " \
        # "ELSE 'UNKNOWN' END as result " \
        # "FROM timee")

        # cr.execute("SELECT id, name, CASE WHEN number >= 10 THEN 'GOOD' " \
        # "WHEN number = 24 THEN 'Perfect' " \
        # "ELSE 'UNKNOWN' END as result " \
        # "FROM timee")

        # cr.execute("SELECT id, name, CASE WHEN number <= 15 THEN 'GOOD' " \
        # "WHEN number = 24 THEN 'Perfect' " \
        # "ELSE 'UNKNOWN' END as result " \
        # "FROM timee")

        # Anuther way 

        cr.execute("SELECT id, name , number, CASE number WHEN 10 THEN 'NOT BAD' " \
        "WHEN 15 THEN 'GOOD' " \
        "WHEN 24 THEN 'Perfect' " \
        "ELSE 'UNKNOWN' " \
        "END as result " \
        "FROM timee")

        for row in cr.fetchall():

            print(row[0], row[1], row[2], row[3])



    def UPDATE_1(cr):

        cr.execute("UPDATE timee SET number = CASE number WHEN 10 THEN number + 10 " \
        "WHEN 15 THEN number + 15 " \
        "WHEN 24 THEN number + 24 " \
        "ELSE number " \
        "END")



    def SHOW(cr):

        cr.execute("SELECT * FROM timee")

        for row in cr.fetchall():

            print(row[0], row[1], row[2], row[3])

# Calling func:

    # UPDATE(cr)

    # SELECT(cr)

    # UPDATE_1(cr)

    SHOW(cr) 

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()