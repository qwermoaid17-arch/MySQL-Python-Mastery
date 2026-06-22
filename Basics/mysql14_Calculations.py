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

    cr.execute("CREATE TABLE IF NOT EXISTS salary (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), days INT(11), day_salary INT(11))")

    def INSERT(cr):

        cr.execute("INSERT INTO salary (name, days, day_salary) VALUES (%s, %s, %s)",('moayed', 23, 40))

        cr.execute("INSERT INTO salary (name, days, day_salary) VALUES (%s, %s, %s)",('mohamed', 13, 20))

        cr.execute("INSERT INTO salary (name, days, day_salary) VALUES (%s, %s, %s)",('ahmed', 35, 28))

        cr.execute("INSERT INTO salary (name, days, day_salary) VALUES (%s, %s, %s)",('alaa', 45, 30))



    def SELECT_calcultions(cr):

        # cr.execute("SELECT ROUND(21 / 2) AS result")

        # cr.execute("SELECT ROUND(21 % 2) AS result")

        # cr.execute("SELECT ROUND(22 % 2) AS result")

        # cr.execute("SELECT name, days, day_salary FROM salary")

        # cr.execute("SELECT name, days, day_salary, days * day_salary as total_many FROM salary ")

        cr.execute("SELECT name, days, day_salary, (days * day_salary) + 100 as total_many FROM salary ")

        cr.execute("SELECT name, days, day_salary, (days * day_salary) as total_many, (days * day_salary) + 100 as total_many_2, ROUND((days * day_salary) + 100) - 50 FROM salary ")



        for row in cr.fetchall():

            print(row[0], row[1], row[2], row[3], row[4], row[5])



    def SHOW(cr):

        cr.execute("SELECT * FROM salary")

        for row in cr.fetchall():

            print(row[0], row[1], row[2], row[3])

# Calling func:

    # INSERT(cr)

    SELECT_calcultions(cr)

    # SHOW(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()