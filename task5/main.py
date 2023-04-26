import sqlite3 as sq
with sq.connect("court.db") as db :
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS lawyers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                experience INTEGER NOT NULL
               )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS accused (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL, 
                age INTEGER NOT NULL DEFAULT 18
                )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS session (
               id INTEGER NOT NULL UNIQUE,
               id_lawyer INTEGER NOT NULL,
               id_accused INTEGER NOT NULL,
               crime TEXT NOT NULL,
               prison_time TEXT NOT NULL,
               FOREIGN KEY (id_lawyer) REFERENCES lawyers (id),
               FOREIGN KEY (id_accused) REFERENCES accused (id),
               PRIMARY KEY (id_lawyer, id_accused)
               )""")

    #я забыл здесь указать insert'ы =)

    cursor.execute('SELECT * FROM session')
    alldata = cursor.fetchall()
    print(alldata)
    cursor.execute("SELECT id, name FROM accused WHERE name LIKE '%Саламанка%'")
    alldata = cursor.fetchall()
    print(alldata)
    cursor.execute("SELECT * FROM lawyers WHERE experience < 15")
    alldata = cursor.fetchall()
    print(alldata)


