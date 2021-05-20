money = 5000
predator = 3500
sposob = input('Введите способ оплаты: ')
if sposob == 'Mastercard':
    print('Мы не поддерживаем Mactercard')
elif sposob == 'Elcard':
    print('Мы не поддерживаем Elcard')
elif sposob.lower() == 'Visa'.lower() or sposob.lower() == 'Paypal'.lower() or sposob.lower() == 'Sberbank'.lower():
    print('Введите номер вашей карты')
    a = input('Введите номер: ')
    b = input('Подтвердите карту:')
    if len(a) == 4 and a == b: 
        print('Номер правильный ')
        balance = int(input('Введите сумму: '))
        if predator > money and balance > 0 and balance <= money:
            print('недостаточно суммы')
        elif predator < money and balance > 0 and balance <= money:
            print('У вас осталось: ', money - balance)
    else:
        print('Неправильно ')
        print('Вторая попытка')
        a = input('Введите номер: ')
        b = input('Подтвердите карту:')
        if len(a) == 4 and a == b:
            print('Номер правильный')
            balance = int(input('Введите сумму'))
            if predator > money:
                print('недостаточно суммы')
            elif predator < money:
                print('У вас осталось: ', money - balance)
        else:
            print('Повторите попытку')
            print('Третья попытка ')
            a = input('Введите номер: ')
            b = input('Подтвердите карту:')
            if len(a) == 4 and a == b:
                print('Номер правильный')
                balance = int(input('Введите сумму'))
                if predator > money:
                    print('недостаточно суммы')
                elif predator < money:
                    print('У вас осталось: ', money - balance)
            else:
                print('Повторите попытку')
                print('Четвертая попытка')
                if len(a) == 16 and a == b:
                    print('Номер правильный')
                    balance = int(input('Введите сумму'))
                    if predator > money:
                        print('недостаточно суммы')
                    elif predator < money:
                        print('У вас осталось: ', money - balance)
                else:
                    print('Вы получили Бан')
else:
    print('не гони')