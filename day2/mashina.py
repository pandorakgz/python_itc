
#  cars = []
#  car = ''
#  car = input('1 mashina: ')
#  cars.append(car)

#  car = input('2 mashina: ')
#  cars.append(car)

#  car = input('3 mashina: ')
#  cars.append(car)

#  car = input('4 mashina: ')
#  cars.append(car)

#  car = input('5 mashina: ')
#  cars.append(car)

#  print('наши машины: ',cars)

#  s = input('выберите машину:')
#  print('Поздравляю:', s ,'это вам подарок.')
cars = [ 
 'mers',
 'bmw',
 'volvo',
 'honda',
 'hyndai']
print('Биздин машиналар: ', cars)
rs = input('Машина танданыз: ')

if rs == cars[0] or rs == cars[1] or rs == cars[2] or rs == cars[3] or rs == cars[4]:
    
    print('Куттуктайм:', rs,'Машина сизге белек.')
else:
    print('Бизде андай машина жок: ')