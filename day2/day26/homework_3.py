# Problem3

# Напишите программу с классом Car. Создайте конструктор класса Car. 
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год). 
# Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. 
# Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.

class Car:
    def __init__(self, name, type, year,color):
        self.name = name
        self.type = type
        self.year = year
        self.color = color

    def auto_on(self):
        print(self.name,'\n',
        'Автомобиль заведен')

    def auto_off(self):
        print(self.name,'\n',
        'Автомобиль заглушен')

    def auto_year(self):
        print('Год вашего автомабиля: ', self.year)

    def auto_color(self):
        print('Цвет вашего автомабиля', self.color)

    def auto_type(self):
        print('Тип вашего автомабиля', self.type)


honda = Car(
    name = 'streem',
    type = 'universal',
    year = '2002',
    color = 'blue'
)



tayota = Car(
    name = 'streem',
    type = 'universal',
    year = '2002',
    color = 'blue'
)


mazda = Car(
    name = 'rx6',
    type = 'sport',
    year = '2019',
    color = 'red'
)



nissan = Car(
    name = 'primera',
    type = 'universal',
    year = '2003',
    color = 'white'
)



shevrale = Car(
    name = 'carvet',
    type = 'sport',
    year = '2019',
    color = 'black'
)

