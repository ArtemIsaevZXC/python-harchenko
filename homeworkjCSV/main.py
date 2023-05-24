import csv
import datetime
import locale

locale.setlocale(locale.LC_ALL, "Russian")

filename = "9 - 1.csv"  # Название файла
with open(filename, encoding="utf-8") as file:
    file_reader = csv.reader(file, delimiter=",")

    header = next(file_reader)

    if filename == "9 - 2.csv":
        try:
            end_index = header.index("Завершено")
            test_started_index = header.index("Тест начат")
            name_index = header.index("Фамилия")
            surname_index = header.index("Имя")
            score_indices = []
            for i in range(10):
                score_column = f"В. {i + 1} /10,00"
                if score_column in header:
                    score_indices.append(header.index(score_column))
                else:
                    break
            max_score = 10.0
        except ValueError:
            print("Некорректный формат файла")
            exit(1)
    elif filename == "9 - 1.csv":
        try:
            end_index = header.index("Завершено")
            test_started_index = header.index("Тест начат")
            name_index = header.index("Фамилия")
            surname_index = header.index("Имя")
            score_indices = []
            for i in range(10):
                score_column = f"В. {i + 1} /1,00"
                if score_column in header:
                    score_indices.append(header.index(score_column))
                else:
                    break
            max_score = 1.0
        except ValueError:
            print("Некорректный формат файла")
            exit(1)
    else:
        print("Недопустимое название файла")
        exit(1)

    listeners = {}

    for row in file_reader:
        end = " ".join(str(row[end_index]).split())
        if end == "-" or end == "":
            continue

        locale.setlocale(locale.LC_TIME, "Russian")
        end_date = datetime.datetime.strptime(end, "%d %B %Y %H:%M")
        locale.setlocale(locale.LC_TIME, "")

        scores = [float(str(row[index]).replace(",", ".")) for index in score_indices]
        total_score = sum(scores)

        if total_score >= 0.6 * max_score:
            locale.setlocale(locale.LC_TIME, "Russian")
            test_started = datetime.datetime.strptime(row[test_started_index], "%d %B %Y %H:%M")
            locale.setlocale(locale.LC_TIME, "")

            name = row[name_index]
            surname = row[surname_index]

            if (surname, name) not in listeners:
                listeners[(surname, name)] = {
                    "name": name,
                    "surname": surname,
                    "test_started": test_started,
                    "score": total_score
                }
            else:
                if listeners[(surname, name)]["score"] < total_score:
                    listeners[(surname, name)]["test_started"] = test_started
                    listeners[(surname, name)]["score"] = total_score

    sorted_listeners = sorted(listeners.values(), key=lambda x: x["test_started"])

    for listener in sorted_listeners:
        print(listener["surname"], listener["name"], listener["test_started"], listener["score"])
