# # f.remove("")udalit
# # f.pop("6")udaliti po indeksu
# # f.extend("")obedenit
# cars = ( 
# 'mers',
# 'bmw',
# 'volvo',
# 'honda',
# 'hyndai')
# print('Биздин машиналар: ')
# print(cars)
# rs = input('Машина танданыз: ')
# print('Куттуктайм:', rs,'Машина сизге белек.')
# cars = []
# car = ''
# car = input('1 mashina: ')
# cars.append(car)

# car = input('2 mashina: ')
# cars.append(car)

# car = input('3 mashina: ')
# cars.append(car)

# car = input('4 mashina: ')
# cars.append(car)

# car = input('5 mashina: ')
# cars.append(car)

# print('наши машины: ',cars)

# s = input('выберите машину:')
# print('Поздравляю:', s ,'это вам подарок.')
# text = '''Степан Аркадьич взял шляпу и остановился, припоминая, не забыл ли чего. 
# Оказалось, что он ничего не забыл, кроме того, что хотел забыть, — жену.
# "Ах да!" Он опустил голову, и красивое лицо его приняло тоскливое выражение. 
# "Пойти или не пойти?" — говорил он себе. И внутренний голос говорил ему, что ходить не надобно, что, кроме фальши,
# тут ничего быть не может, что поправить, починить их отношения невозможно, потому что невозможно сделать ее опять
# привлекательною и возбуждающею любовь или его сделать стариком, не способным любить. Кроме фальши и лжи,
# ничего не могло выйти теперь; а фальшь и ложь были противны его натуре.
# '''

# words = text.split('.')
# print(words)
# print(len(words))
# print(words[10])


# text = '''
#     Степан Аркадьич взял шляпу и остановился, припоминая, не забыл ли чего. 
#     Оказалось, что он ничего не забыл, кроме того, что хотел забыть, — жену.
# "Ах да!" Он опустил голову, и красивое лицо его приняло тоскливое выражение. 
# "Пойти или не пойти?" — говорил он себе. И внутренний голос говорил ему, 
# что ходить не надобно, что, кроме фальши, тут ничего быть не может, что поправить,
#  починить их отношения невозможно, потому что невозможно сделать ее опять привлекательною и возбуждающею любовь или его сделать стариком, 
#  не способным любить. Кроме фальши и лжи, ничего не могло выйти теперь;
#   а фальшь и ложь были противны его натуре.
# '''

# words = text.split('.')
# print(len(words))
# # 1. Жогорудагы тексти, суйломдун жыйындысынан турган sentences тизмеге айлант жана 
# # экранга чыгарып бер.
# # 2. text канча суйлом бар ошону эсептеп экранга чыгар.

# 1. Жогорудагы эки тизмени бириктир.
# 2. input аркылуу 3 жер жемиш тизмеге кош.
# 3. 1 индекстеги элементи очур.

fruits = ['алма', 'вишня', 'орук', "дарбыз", "кулпунай"]
eats = ['суу', 'аш', 'шорпо', 'лагман','самса','нан','куурдак','чай']



eat = input('1 жемиш: ')
eats.append(eat)
eat = input('2 жемиш: ')
eats.append(eat)
eat = input('3 жемши: ')
eats.append(eat)

fruits.append(eats)
print(fruits)

































