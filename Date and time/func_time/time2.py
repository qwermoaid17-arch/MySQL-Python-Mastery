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

    cr.execute("CREATE TABLE IF NOT EXISTS time (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), date DATE)")

    def insert_user(cr):

        cr.execute("INSERT INTO time (name, date) VALUES (%s, %s)", ("maoyed", "2026-7-30"))

        cr.execute("INSERT INTO time (name, date) VALUES (%s, %s)", ("ahmed", "2028-8-30"))

        cr.execute("INSERT INTO time (name, date) VALUES (%s, %s)", ("mohamed", "2024-6-30"))

    def SELECT_time(cr):

        # cr.execute("SELECT CURTIME()")

        # cr.execute("SELECT CURTIME() as today , DAYNAME(CURDATE()) as day_name")

        # cr.execute("SELECT CURDATE() as today ,DAYNAME('2023-08-22') as day_name")

        # cr.execute("SELECT id,name, date, DAYNAME(date) as day_name FROM time")

        # cr.execute("SELECT id,name, date, DAYNAME(date) as day_name, MONTHNAME(date) as month FROM time")

        cr.execute("SELECT id,name, date, DAYNAME(date) as day_name, MONTHNAME(date) as month, DAYOFWEEK(date) as day_of_week , DAYOFYEAR(date) as day_of_year FROM time")



        result = cr.fetchall()

        for i in result:

            print(f"{i[0]} / / {i[1]} // {i[2]} // {i[3]} // {i[4]} // {i[5]} // {i[6]}")

    def DELETE_time(cr):

        cr.execute("DELETE FROM time WHERE id BETWEEN 10 AND 12")

    def rename_name_table(cr):

        #  for changing the word "reserved"

        cr.execute("RENAME TABLE time TO timee")

    #CALLING THE FUNCTION : 

    # insert_user(cr)

    # DELETE_time(cr)

    # rename_name_table(cr)

    SELECT_time(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()