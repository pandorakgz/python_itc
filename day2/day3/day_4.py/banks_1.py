banks = [
    {
        "name": 'Demir Bank',
        'balans' : 50000.00,
        'voluta' : 'KGS',
        'pin' : 3342
    },
    {
        "name": 'Optima Bank',
        'balans' : 99000.00,
        'voluta' : 'Usa',
        'pin' : 3322
    },
    {
        "name": 'KICB',
        'balans' : 53300.00,
        'voluta' : 'KGS',
        'pin' : 3324
    },
    {
        "name": 'Dos-Credo Bank',
        'balans' : 45000.00,
        'voluta' : 'USA',
        'pin' : 3433
    },
]

curs = {
    'EUR' : '101.65',
    'USD' : 84.80,
    'RUS' : 1.23,
    'KZT' : 0.010
}
print('moi akkaunty')
for index in range(4):
    print(index + 1, ':', banks[index]['name'])

vybor = int(input('Выберите аккаунт: '))

if vybor < 5 and vybor >= 1:
    rindex = vybor - 1
    print(banks[rindex]['name'])
    pin =int(input('Пин котту териниз: '))


    if pin == banks[rindex]['pin']:
        print('Добро пожаловать')
        print('Ваш баланс: ', banks[rindex]['name'],banks[rindex]['balans'])
    else:
        print('пароль не верный')
else:
    print('Андай аккаунт жок')