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



    def SELECT_time(cr):

        # cr.execute("SELECT date , DATEDIFF(CURDATE(), date) as days FROM timee")

        cr.execute("SELECT date , CONCAT(' registered ', DATEDIFF(CURDATE(), date) , ' days ago') as days FROM timee")


        result = cr.fetchall()

        for i in result:

            print(f"{i[0]} // {i[1]}")


    SELECT_time(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()