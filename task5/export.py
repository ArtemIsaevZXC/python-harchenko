import xml.dom.minidom as minidom
import sqlite3 as sq

root = minidom.Document()
xml = root.createElement('accused')
root.appendChild(xml)
with sq.connect("court.db") as db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM accused')
    for cur in cursor:
        new_person = root.createElement('person')
        new_person.setAttribute("name", cur[1])
        new_id = root.createElement("id")
        new_id_data = root.createTextNode(str(cur[0]))
        new_id.appendChild(new_id_data)
        new_age = root.createElement("age")
        new_age_data = root.createTextNode(str(cur[2]))
        new_age.appendChild(new_age_data)
        new_person.appendChild(new_id)
        new_person.appendChild(new_age)
        xml.appendChild(new_person)
out_byte = root.toprettyxml(encoding='UTF-8')
out_text = out_byte.decode("UTF-8")
save_path_file = "data1.xml"
with open(save_path_file, "w", encoding="UTF-8") as f:
    f.write(out_text)
f.close()

