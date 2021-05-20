correct_pin = 1203 
balance = 5000
print('Добро пожаловать')
pin = int(input('Введите пин код: '))


if pin == correct_pin:
    print('1. Проверка баланса')
    print('2. Снятие')
    print('1. Поменять Операцию')
    operation = int(input('Выберите операцию: '))
    if operation == 2:
        summa = int(input('Сколько хотите денег?'))
        if summa > (balance - 100):
            print('У вас недостаточно средств')
        else:
            balance = balance - summa
            print('Дерьги сняты с вашего баланса ', balance)
    elif operation == 3:
        newpin = int(input('Введите новый пароль: '))
        new_pin = int(input('Повторите пароль: '))
        if newpin != new_pin:
            print('Ошибка')
        else:
            correct_pin = newpin
            print('Пин был изменен0')
            pin_1 = int(input('Проверка Пин кода: '))
            if pin_1 != correct_pin:
                print('Вы получил бан')
            else:
                print('Пин был сменен')
else:
    print('Неверный пароль')