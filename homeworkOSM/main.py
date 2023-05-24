import xmltodict

with open('9 - 2.osm', 'r', encoding='utf-8') as f:
    dct = xmltodict.parse(f.read())

pharmacy_count = 0
full_day_pharmacy_count = 0
pharmacies = []

for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            pharmacy_tag_found = False
            name = ''
            opening_hours = ''
            for tag in tags:
                if tag['@k'] == 'amenity' and tag['@v'] == 'pharmacy':
                    pharmacy_count += 1
                    pharmacy_tag_found = True
                elif tag['@k'] == 'name':
                    name = tag['@v']
                elif tag['@k'] == 'opening_hours':
                    opening_hours = tag['@v']
            if pharmacy_tag_found:
                if opening_hours == '24/7':
                    full_day_pharmacy_count += 1
                lat = node['@lat']
                lon = node['@lon']
                pharmacies.append((name, lat, lon))

pharmacies_sorted = sorted(pharmacies, key=lambda x: x[0])  # Сортировка по имени

print("Количество аптек:", pharmacy_count)
print("Количество круглосуточных аптек:", full_day_pharmacy_count)
print("Аптеки в алфавитном порядке:")
for pharmacy in pharmacies_sorted:
    name, lat, lon = pharmacy
    if name:
        print(f"Название: {name}, Координаты: ({lat}, {lon})")
    else:
        print(f"Название: Неизвестно, Координаты: ({lat}, {lon})")
