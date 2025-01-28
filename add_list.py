username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'дд-мм-гг': ")
issue_date = input("Введите дату истечения заметки в формате 'дд-мм-гг': ")

temp_created_date = created_date
temp_issue_date = issue_date

titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)

print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Заголовки заметки:", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_created_date[0:5:1])
print("Дата истечения заметки:", temp_issue_date[0:5:1])



