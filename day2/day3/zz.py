car_len = 16
sposob = input('Введите способ оплаты: ')
if sposob == 'Mastercard':
    print('Мы не поддерживаем Mactercard')
elif sposob == 'Elcard':
    print('Мы не поддерживаем Elcard')
elif sposob.lower() == 'Visa'.lower() or sposob.lower() == 'Paypal'.lower() or sposob.lower() == 'Sberbank'.lower():
    print('Введите номер вашей карты')
    a = int(input('Введите номер: '))
    if len(a) == 16:
        print('Оплата произведена')
    else:
        print('повторите попытку')
        print('Вторая попытка')
        a = int(input('Введите номер: '))
        if len(a) == 16:
            print('Оплата произведена')
        else:
            print('повторите попытку')
            print('третья попытка ')
            a = int(input('Введите номер: '))
            if len(a) == 16:
                print('Оплата произведена')
            else:
                print('повторите попытку')
                print('четвертая попытка')
                if len(a) == 16:
                    print('Оплата произведена')
                else:
                    print('Вы получили Бан')
else:
    # print('не гони')
    #     print(a,'/',2,'=',a / 2)
    # print(a,'/',3,'=',a / 3)
    # print(a,'/',4,'=',a / 4)
    # print(a,'/',5,'=',a / 5)
    # print(a,'/',6,'=',a / 6)
    # print(a,'/',7,'=',a / 7)
    # print(a,'/',8,'=',a / 8)
    # print(a,'/',9,'=',a / 9)
    # print(a,'/',10,'=',a / 10)