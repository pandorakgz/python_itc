# class Human:
#     name = ''
#     color = ''
#     rassa = ''
#     gender = ''
#     weight = ''
#     age = ''
#     hair = ''
#     hair_color = ''
#     def to_walk(self):
#         print(self.name, 'Баса алат')
    
#     def to_speak(self, word, word2):
#         print(self.name, 'govorit', word, word2)


# belek = Human()
# belek.name = 'Белек'
# belek.color = 'Будай цветтуу'
# belek.rassa = 'Кыргыз'

# belek.to_walk()
# belek.to_speak('Салам кандай ?', 'Жакшы озун')


ai_92 = 49.50
ai_95 = 51.50

class Car:
    rasxod_100 = 12
    def __init__(self, name, year, color, volume):
        self.name = name
        self.year = year
        self.color = color
        self.volume = volume
    
    def get_volume(self):
        print('Мой обьем:', self.volume)

    def get_rasxod(self, km):
        r = (km / 100) * self.rasxod_100
        print('Расход на', km, r)

    def get_rasxod_price(self, km):
        d = (km / 100) * self.rasxod_100*ai_95
        s = (km / 100) * self.rasxod_100*ai_92
        print('Расход на 95', km, d)
        print('Расход на 92', km, s)


mycar = Car(
    name = 'Matiz 1', 
    year = 2000,
    color = 'Белый',
    volume = 3.5
)

mycar.get_volume()
mycar.get_rasxod(40)
mycar.get_rasxod_price(100)