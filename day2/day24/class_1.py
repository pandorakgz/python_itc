class Panda:
    name = input('Введите имя Панды: ')
    weight = int(input('Введите вес Панды: '))
    age = int(input('Введите возраст Панды: '))
    color = input('Введите цвет Панды: ')
    speed = int(input('Введите скорость Панды: '))
    power = int(input('Введите мощность Панды: '))
    def to_walk(self):
        print('Томолоп кеттат')



panda = Panda()
print('Имя Панды', panda.name)
print('Вес Панды', panda.weight)
print('Скорость Панды', panda.speed)
print('Мощность Панды', panda.power)
print('Цвет Панды', panda.color)
print('Возраст Панды', panda.age)
panda.to_walk()