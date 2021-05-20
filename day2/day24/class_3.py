class Animal:
    def __init__(self,**kwargs):
        self.name = kwargs['name']
        self.type = kwargs['type']
        self.speed = kwargs['speed']
        # self.name = kwargs['name']
        # self.name = kwargs['name']
    def get_speed(self):
        print('Бегает {} km в час'.format(self,speed))

    def get_full_time(self, km):
        print(km/self.speed)
        

name =input('Введите имя Панды: ')
type = input('Введите тип Панды: ')
speed = int(input('Введите скорость Панды: '))
Panda = Animal(
    name = name,
    type = type,
    speed = speed
)

Panda.get_full_time(400)
    