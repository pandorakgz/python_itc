operators = {
    'megacom': [
        '0558',
        '0551',
        '0555',
        '0557',
        '0996',
        '0550',
    ],
    'beeline': [
        '0770',
        '0777'
    ],
    'Ошка': [
        '0700',
        '0999'
    ]
}
def check_phone_number(nomer):
    if len(nomer) == 10 and nomer[0] == '0':
        print('Номер телефона правильный')
        code = nomer[0:4]
        if code in operators['Ошка']:
            print('Ваш оператор О')
        elif code in operators['megacom']:
            print('Ваш оператор Мегаком')
        elif code in operators['beeline']:
            print('Ваш оператор Белайн')
    else:
        print('Вы ввели неправильный номер')



def translate():
    print('say hello')

def getFullname(fname, lname):
    return fname + ' ' + lname