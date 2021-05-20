# 1.
# Создай Class Teacher
# свойство:
# name - имя учителя
# age - возраст учителя 
# predmet - имя предмет (по какому предмету препод-т)
# создайте функции:
# to_teach(self): - должна показывать по какому предмету обучает
    
# На основое Class Teacher создай обьекты учителей по:
# Физике  
# Биологии
# Математики

# class Teacher:
#     name = input('Введите имя учителя: ')
#     age = int(input('Введите возраст учителя: '))
#     predmet = input('Введите предмет учителя: ')
#     def urok (self):
#         print('Этот учитель преподает ',self.predmet )
    



# uch = Teacher()
# print('Имя учителя', uch.name)
# print('Возраст учителя', uch.age)
# uch.urok()



# 2.
# Создай Обьект Plane реализуй его свойство и умение летать


# class Plane():
#     rasxod_100 = 120
#     name =input('Введите имя самолета: ')
#     year = int(input('Введите год самолета: '))
#     color = input('Введите цвет самолета: ')
#     volume = int(input('Введите объем самолета: '))
#     length = int(input('Введите длину самолета: '))
#     def get_volume(self):
#         print('Мой обьем:', self.volume)
#     def technik_fling(self):
#         print(self.name, 'умеет летать')
#     def get_rasxod(self, km):
#         r = (km / 100) * self.rasxod_100
#         print('Расход на', km,'km', r,'литров')

# uchak = Plane()
# uchak.get_volume()
# uchak.technik_fling()
# uchak.get_rasxod(500)



# 3.
# Создай Обьект Hacker реализуй все его свойство и умение 
# Характеристики:
# уровень - уровень хакера
# навыки - какими навыками он обладает
# возраст - возраст хакера
# пол

# Что он может делать ?
# Например: взломать почту, взлом сайта, взлом сети




# class Hacker:
#     level = input('Введите уровень Хакера: ')
#     attainments = input('Введите ЯП который Хакер знает: ')
#     age = int(input('Введите возраст Хакера: '))
#     gender = input('Введите пол Хакера: ')
#     def what_he_can(self):
#         print(self.level, 'может взломать этот сайт')

#     def what_he_can_do(self):
#         print(self.level,' может взломать этот E-mail')   

#     def he_can(self):
#         print(self.level, 'может взломать этот сеть')  
# hackerr =  Hacker()


# hackerr.what_he_can()
# hackerr.what_he_can_do()
# hackerr.he_can()