#1
class Robot:
    def __init__(self, name, model):
        self.name = name    # Сохраняем имя
        self.model = model  # Сохраняем модель

# При создании объекта мы передаем аргументы в __init__
r1 = Robot("R2-D2", "Astromech")
print(r1.name) # Выведет: R2-D2
#2
class Cat:
    def __init__(self, name):
        self.name = name

    # Метод экземпляра
    def say_meow(self):
        print(f"{self.name} говорит: Мяу!")

my_cat = Cat("Барсик")
my_cat.say_meow()  # self подставится автоматически
#3
class Car:
    wheels = 4  # Переменная класса (у всех машин 4 колеса)

    def __init__(self, color):
        self.color = color  # Переменная экземпляра (цвет у всех разный)

car1 = Car("Красный")
car2 = Car("Синий")

print(car1.wheels) # 4
print(car1.color)  # Красный
#4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Иван", 20)

# 1. Модификация (Изменение)
p1.age = 21 

# 2. Удаление свойства
del p1.age 

# 3. Удаление самого объекта
del p1