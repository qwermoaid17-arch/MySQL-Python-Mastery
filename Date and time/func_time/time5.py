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



    def SELECT_LAST_DAY(cr):

        # cr.execute("SELECT LAST_DAY(date) FROM timee")

        cr.execute("SELECT LAST_DAY(date) as last_day, DAYNAME(last_day(date)) as last_day_name  FROM timee")

        # cr.execute("SELECT date FROM timee where date BETWEEN date  AND LAST_DAY(date) ")

        for row in cr.fetchall():

            print(row[0], row[1])


    def update_date(cr):

        
        # cr.execute("UPDATE timee SET date = DATE_ADD(date, INTERVAL 10 DAY)")

        cr.execute("UPDATE timee SET date = DATE_ADD(date, INTERVAL 1 MONTH)")

    def show(cr):

        cr.execute("SELECT date FROM timee")

        for row in cr.fetchall():

            print(row[0])

    def UPDATE_SUB(cr):

        cr.execute("UPDATE timee SET date = DATE_SUB(date, INTERVAL 3 MONTH)")

    SELECT_LAST_DAY(cr)

    # update_date(cr)

    # UPDATE_SUB(cr)

    # show(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()