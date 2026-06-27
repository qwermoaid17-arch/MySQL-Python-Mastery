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

    def INSERT(cr):

        cr.execute("INSERT INTO lang (name_lang) VALUES (%s)", ("Python",))

        cr.execute("INSERT INTO user (name_user, lang_id) VALUES (%s, %s)", ("Ahmed", 1))

        cr.execute("INSERT INTO lang (name_lang) VALUES (%s)", ("Java",))

        cr.execute("INSERT INTO user (name_user, lang_id) VALUES (%s, %s)", ("Moayed", 2))

        cr.execute("INSERT INTO lang (name_lang) VALUES (%s)", ("C++",))

        cr.execute("INSERT INTO user (name_user, lang_id) VALUES (%s, %s)", ("Alaa", 3))

        cr.execute("INSERT INTO lang (name_lang) VALUES (%s)", ("C#",))

        cr.execute("INSERT INTO lang (name_lang) VALUES (%s)", ("PHP",))




    def join(cr):

        # cr.execute("SELECT * FROM user join lang")

        # cr.execute("SELECT * FROM user, lang")

        cr.execute("SELECT * FROM user , lang WHERE user.lang_id = lang.id")

        for row in cr.fetchall():

            print(row)

    def Alias(cr):

        cr.execute("SELECT u.id as user_id," \
        "  u.name_user as user_name," \
        " u.lang_id as user_lang_id," \
        " l.id as lang_id," \
        " l.name_lang as lang_name " \
        "FROM user as u, lang as l " \
        "WHERE u.lang_id = l.id")

        for row in cr.fetchall():

            print(row)
# Calling func:

    # INSERT(cr)

    # join(cr)

    Alias(cr)

    # SHOW(cr)

    db.commit()

except sql.Error as er:

    print("Error ", er)

finally:

    if db:

        db.close()