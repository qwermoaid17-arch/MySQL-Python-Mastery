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

    def INSERT_time(cr):

        # cr.execute("INSERT INTO timee (name, date) VALUES (%s, NOW())", ("mohab"))

        cr.execute("INSERT INTO timee (name, date) VALUES (%s, %s)", ("mohab", "2024-6-30 12:30:45"))



    def SELECT_time(cr):

        # cr.execute("SELECT date , MONTH(date) as month FROM timee")


        # cr.execute("SELECT date , MONTH(date) as month, MONTHNAME(date) as month_name FROM timee")


        # cr.execute("SELECT date , MONTH(date) as month, MONTHNAME(date) as month_name, HOUR(date) as hour FROM timee")


        cr.execute("SELECT date , MONTH(date) as month, MONTHNAME(date) as month_name, HOUR(date) as hour , MINUTE(date) as minute FROM timee")



        result = cr.fetchall()

        for i in result:

            print(f"{i[0]} // {i[1]} // {i[2]} // {i[3]} // {i[4]}")

    def ALTER_time(cr):

        cr.execute("ALTER TABLE timee CHANGE date date DATETIME")

    #CALLING THE FUNCTION :

    # ALTER_time(cr)

    # INSERT_time(cr)

    SELECT_time(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()