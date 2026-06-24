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

    cr.execute("CREATE TABLE IF NOT EXISTS groupp (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, point INT(11) NOT NULL)")

    cr.execute("CREATE TABLE IF NOT EXISTS orders (id INT AUTO_INCREMENT PRIMARY KEY, status VARCHAR(100) NOT NULL)")



    def INSERT(cr):

        cr.execute("INSERT INTO groupp (name, point) VALUES (%s, %s)", ("ahmed", 100))

        cr.execute("INSERT INTO groupp (name, point) VALUES (%s, %s)", ("moayed", 200))

        cr.execute("INSERT INTO groupp (name, point) VALUES (%s, %s)", ("mohamed", 300))

        cr.execute("INSERT INTO groupp (name, point) VALUES (%s, %s)", ("alaa", 400))

        cr.execute("INSERT INTO groupp (name, point) VALUES (%s, %s)", ("alaa", 500))

        cr.execute("INSERT INTO groupp (name, point) VALUES (%s, %s)", ("ahmed", 600))

        cr.execute("INSERT INTO groupp (name, point) VALUES (%s, %s)", ("ziyad", 700))

        cr.execute("INSERT INTO groupp (name, point) VALUES (%s, %s)", ("mona", 800))

    def INSERT_orders(cr):

        cr.execute("INSERT INTO orders (status) VALUES (%s)", ("pending"))

        cr.execute("INSERT INTO orders (status) VALUES (%s)", ("pending"))

        cr.execute("INSERT INTO orders (status) VALUES (%s)", ("pending"))

        cr.execute("INSERT INTO orders (status) VALUES (%s)", ("aproved"))

        cr.execute("INSERT INTO orders (status) VALUES (%s)", ("canceled"))

        cr.execute("INSERT INTO orders (status) VALUES (%s)", ("canceled"))

        cr.execute("INSERT INTO orders (status) VALUES (%s)", ("canceled"))

        cr.execute("INSERT INTO orders (status) VALUES (%s)", ("on kichen"))


    def delete(cr):

        cr.execute("DELETE FROM groupp WHERE id BETWEEN  %s and %s", (9,20))

    def orderd_select(cr):

        cr.execute("SELECT * From groupp ORDER BY name")

        cr.execute("SELECT * From groupp ORDER BY name DESC")

        cr.execute("SELECT * From groupp ORDER BY name, point")

    def Group_by_select(cr):

        # cr.execute("SELECT * From groupp GROUP BY name")

        # cr.execute("SELECT name, sum(point) as pointed FROM groupp GROUP BY name ORDER BY pointed")

        # cr.execute("SELECT name, sum(point) as pointed FROM groupp GROUP BY name ORDER BY pointed DESC")

        # cr.execute("SELECT status FROM orders GROUP BY status")

        # cr.execute("SELECT status, count(status) as how_match FROM orders GROUP BY status ORDER BY how_match ")

        cr.execute("SELECT status, count(status) as how_match FROM orders GROUP BY status having how_match > 1")

        for row in cr.fetchall():

            print(row[0], row[1])

    def SHOW(cr):

        cr.execute("SELECT * FROM groupp")

        for row in cr.fetchall():

            print(row[0], row[1], row[2])


    def shows(cr):

        cr.execute("SHOW TABLES")

        for row in cr.fetchall():

            print(row[0])

# Calling func:

    # INSERT(cr)

    # delete(cr)

    # orderd_select(cr)

    # INSERT_orders(cr)

    Group_by_select(cr)

    # SHOW(cr)

    # shows(cr)


    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()