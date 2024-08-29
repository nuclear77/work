#task1
# def multiply_numbers(a, b):
#     return a * b
#
# result = multiply_numbers(3, 4)
# print("Произведение:", result)


# task2
# with open("test.txt", "w") as file:
#     file.write("Это тестовый файл для домашнего задания по программированию")
#
# with open("test.txt", "r") as file:
#     content = file.read()
#     print("Содержимое файла:", content)


# task3
# import os
#
# os.makedirs("mydir", exist_ok=True)
#
# os.chdir("mydir")
# open("file1.txt", "w").close()
# open("file2.txt", "w").close()
# open("file3.txt", "w").close()
#
# files = os.listdir(".")
# print("Список файлов в 'mydir':", files)


# task4
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

users = [
    {"name": "Иван", "email": "ivan@example.com"},
    {"name": "Мария", "email": "maria@example.com"},
    {"name": "Петр", "email": "petr@example.com"}
]

output = template.render(users=users)
print(output)