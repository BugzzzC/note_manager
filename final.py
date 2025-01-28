note = {}

note["Имя пользователя:"] = input("Введите имя пользователя: ")
note["Описание заметки"] = input("Введите описание заметки: ")
note["Статус заметки"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'дд-мм-гг': ")
issue_date = input("Введите дату истечения заметки в формате 'дд-мм-гг': ")


note["Дата создания заметки"] = created_date[0:5:1]
note["Дата истечения заметки"] = issue_date[0:5:1]

note["Заголовки заметки"] = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    note["Заголовки заметки"].append(title)

print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
