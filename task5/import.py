import xml.dom.minidom as minidom
import sqlite3 as sq

file = open('data.xml', encoding='UTF-8')
dom = minidom.parse(file)
dom.normalize()
elements = dom.getElementsByTagName('person')
name = []
id = []
age = []
for node in elements:
    name_attr = node.getAttribute("name")
    name.append(name_attr)
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'id':
                id.append(child.firstChild.data)
            if child.tagName == 'age':
                age.append(child.firstChild.data)

with sq.connect("court.db") as db:
    cursor = db.cursor()
    for i in range(len(name)):
        cursor.execute('INSERT INTO accused VALUES(?,?,?)', (id[i],name[i],age[i]))
        db.commit()
file.close()



