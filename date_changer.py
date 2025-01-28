username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'дд-мм-гг': ")
issue_date = input("Введите дату истечения заметки в формате 'дд-мм-гг': ")

temp_created_date = created_date
temp_issue_date = issue_date

print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_created_date[0:5:1])
print("Дата истечения заметки:", temp_issue_date[0:5:1])



