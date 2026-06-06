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

    # cr.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(100))")

    def SELECT_time(cr):

        # cr.execute("SELECT CURTIME()")

        # Another way

        # cr.execute("SELECT CURRENT_TIME()")

        # Another way

        cr.execute("SELECT CURRENT_TIME")

        result = cr.fetchall()

        print(result[0][0])
    
    def SELECT_date(cr):

        # cr.execute("SELECT CURDATE()")

        # Another way

        # cr.execute("SELECT CURRENT_DATE()")

        # Another way

        cr.execute("SELECT CURRENT_DATE")

        result = cr.fetchall()

        print(result[0][0])

    def SELECT_datetime(cr):

        # cr.execute("SELECT NOW()")

        # Another way

        # cr.execute("SELECT CURRENT_TIMESTAMP()")

        # Another way

        cr.execute("SELECT CURRENT_TIMESTAMP")

        result = cr.fetchall()

        print(result[0][0])
    
    # Calling func:

    # SELECT_time(cr)

    # SELECT_date(cr)

    SELECT_datetime(cr)

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()