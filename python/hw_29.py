#task1
# import math
#
#
# class Circle:
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def circumference(self):
#         return 2 * math.pi * self.radius
#
#
# circle1 = Circle(5, "red")
# circle2 = Circle(10, "blue")
#
# print(f"Площадь круга 1: {circle1.area()}")
# print(f"Длина окружности круга 1: {circle1.circumference()}")
#
# print(f"Площадь круга 2: {circle2.area()}")
# print(f"Длина окружности круга 2: {circle2.circumference()}")


# task2
# class BankAccount:
#     def __init__(self, account_number, owner_name, balance=0):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Недостаточно средств")
#
#
# account1 = BankAccount("123456", "Иван Иванов", 1000)
# account2 = BankAccount("654321", "Мария Петрова", 500)
#
# account1.deposit(200)
# account1.withdraw(150)
# print(f"Баланс счета 1: {account1.balance}")
#
# account2.deposit(300)
# account2.withdraw(800)
# print(f"Баланс счета 2: {account2.balance}")


# task3
# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
#
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
#
#     def status(self):
#         avg = self.average_grade()
#         if avg >= 4.5:
#             return "Отличник"
#         elif avg >= 3.5:
#             return "Хорошист"
#         else:
#             return "Троечник"
#
#
# student1 = Student("Иван", 20, [4, 5, 5])
# student2 = Student("Мария", 22, [3, 4, 4])
#
# print(f"Средний балл студента 1: {student1.average_grade()}, статус: {student1.status()}")
# print(f"Средний балл студента 2: {student2.average_grade()}, статус: {student2.status()}")


# task4
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def get_info(self):
#         return f"{self.title} by {self.author}, {self.year}"
#
#     def set_info(self, title=None, author=None, year=None):
#         if title:
#             self.title = title
#         if author:
#             self.author = author
#         if year:
#             self.year = year
#
#
# book1 = Book("Война и мир", "Лев Толстой", 1869)
# book2 = Book("Преступление и наказание", "Федор Достоевский", 1866)
#
# print(book1.get_info())
# print(book2.get_info())
#
# book1.set_info(year=1870)
# print(book1.get_info())


# task5
class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def get_info(self):
        return f"{self.brand} {self.model}, {self.color}, {self.year}"

    def set_info(self, brand=None, model=None, color=None, year=None):
        if brand:
            self.brand = brand
        if model:
            self.model = model
        if color:
            self.color = color
        if year:
            self.year = year


car1 = Car("Toyota", "Camry", "черный", 2020)
car2 = Car("Honda", "Civic", "белый", 2019)

print(car1.get_info())
print(car2.get_info())

car1.set_info(color="красный")
print(car1.get_info())