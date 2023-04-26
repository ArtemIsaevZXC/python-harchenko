#!/usr/bin/env python3
import cgi
import sqlite3 as sq
form = cgi.FieldStorage()
n_l = form.getfirst("name_l")
exp = form.getfirst("exp")
n_a = form.getfirst("name_a")
age = form.getfirst("age")
print("Content-type: text/html; charset=utf-8\n")
if (n_l and exp ):
    print(f"{n_l} -> {exp}")
    with sq.connect("court.db") as db:
        cursor = db.cursor()
        cursor.execute('INSERT INTO lawyers VALUES(NULL,?,?)', (n_l, exp))
        db.commit()
        print("""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Успех</title>
                        </head>
                        <body>
                            <a href="../../index.html"><p>Назад</p></a>
                            
                            
                        </body>
                        </html>
                """)
        cursor.execute('SELECT *FROM lawyers')
        alldata = cursor.fetchall()
        print(f"""<table>
                   <tr>
                   <td>id</td>
                   <td>ФИО</td>
                   <td>Стаж</td>
                   </tr>""")
        for cur in alldata:
            print(f"""
                     <tr>
                       <td>{cur[0]}</td>
                       <td>{cur[1]}</td>
                       <td>{cur[2]}</td>
                     </tr>""")
        print("""</table>""")

else:
    if (n_a and age ) :
        print(f"{n_a} -> {age}")
        with sq.connect("court.db") as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO accused VALUES(NULL,?,?)', (n_a, age))
            db.commit()
            print("""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>Успех</title>
                            </head>
                            <body>
                                <a href="../../index.html"><p>Назад</p></a>
                                <p></p>
                            </body>
                            </html>
            """)
            cursor.execute('SELECT *FROM accused')
            alldata = cursor.fetchall()
            print(f"""<table>
            <tr>
            <td>id</td>
            <td>ФИО</td>
            <td>Возраст</td>
            </tr>""")
            for cur in alldata:
                print(f"""
              <tr>
                <td>{cur[0]}</td>
                <td>{cur[1]}</td>
                <td>{cur[2]}</td>
              </tr>""")
            print("""</table>""")


    else:
        print("Форма была не полностью заполнена, попробуйте еще раз")
        print("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>Не получилось</title>
                </head>
                <body>
                    <a href="../../index.html"><p>Назад</p></a>
                </body>
                </html>
        """)




