import pymysql as sql 

try:

    db = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        charset='utf8mb4'
    )

    cr = db.cursor()

    cr.execute("CREATE DATABASE IF NOT EXISTS tests1")

    cr.execute("USE tests1")

    cr.execute("CREATE TABLE IF NOT EXISTS lang(id INT AUTO_INCREMENT PRIMARY KEY, name_lang VARCHAR(100) NOT NULL)")

    cr.execute("CREATE TABLE IF NOT EXISTS user(id INT AUTO_INCREMENT PRIMARY KEY, name_user VARCHAR(100) NOT NULL, lang_id INT NOT NULL, FOREIGN KEY (lang_id) REFERENCES lang(id))")

    def ALTER(cr):

        cr.execute("ALTER TABLE user CHANGE lang_id lang_id INT null")

    def UPDATE(cr):

        cr.execute("UPDATE user SET lang_id = %s WHERE name_user = %s", (1, "Ahmedd"))

    def INSERT(cr):

        cr.execute("INSERT INTO user (name_user) VALUES (%s)", ("Ahmedd",))

        cr.execute("INSERT INTO user (name_user) VALUES (%s)", ("Moayeed",))


    def join(cr):

        # cr.execute("""SELECT u.id as user_id,  
        #            u.name_user as user_name, 
        #            l.name_lang as lang_name
        #            FROM user as u
        #            INNER JOIN 
        #            lang as l
        #            ON
        #             u.lang_id = l.id""")

        cr.execute("""SELECT 
                   l.name_lang as lang_name,
                   count(l.id)
                   FROM user as u
                   INNER JOIN 
                   lang as l
                   ON
                    u.lang_id = l.id 
                   group by l.id""")

        for row in cr.fetchall():

            print(row)


    def join_lift(cr):

        cr.execute("""SELECT u.id as user_id,  
            u.name_user as user_name, 
            l.name_lang as lang_name
            FROM user as u
            LEFT JOIN
            lang as l
            ON
            u.lang_id = l.id""")
        
        for row in cr.fetchall():

            print(row[0], row[1], row[2])

    def join_right(cr):

        cr.execute("""SELECT u.id as user_id,  
            u.name_user as user_name, 
            l.name_lang as lang_name
            FROM user as u
            RIGHT JOIN
            lang as l
            ON
            u.lang_id = l.id""")
        
        for row in cr.fetchall():

            print(row[0], row[1], row[2])


    # ALTER(cr)

    # INSERT(cr)

    # UPDATE(cr)

    # join(cr)

    # join_lift(cr)

    # join_right(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()