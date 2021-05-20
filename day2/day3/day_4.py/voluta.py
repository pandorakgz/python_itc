balance = 300000
print('1.USD = 84.80  KGS')
print('2.EU  = 101.70 KGS')
print('3.KT  = 0.200  KGS')
voluta = int(input('Укажите в какой волюте хотите снять денег: '))
if voluta == 1:
    print("У вас на счету:", balance / 84.80 , 'USD!')
    chek = float(input('Укажите нужную сумму в USD: '))
    if chek > balance / 84.80:
        print('У вас недостаточно средств!')
    else:
        print('Возьмите' , chek , 'USD!' , 'Остаток на карте: ' , balance / 84.80 - chek , 'USD/' ,(balance / 84.80 - chek) * 84.80 , '(SOM)')
if voluta == 2:
    print("У вас на счету:", balance / 101.70 , 'EU')
    chek = float(input('Укажите нужную сумму в EU: '))
    if chek > balance / 101.70:
        print('У вас недостаточно средств!')
    else:
        print('Возьмите' , chek ,'EU!', 'Остаток на карте: ' , balance / 101.70 - chek , ' EU/' ,(balance / 101.70 - chek) * 101.70 , '(SOM)')
if voluta == 3: 
    print("У вас на счету:", balance * 5.10 , 'KT')
    chek = float(input('Укажите нужную сумму в KT: ' ))
    if chek > balance * 5.10:
        print('У вас не достаточно средств!')
    else:
        print('Возьмите' , chek , 'KT!' , 'Остаток на карте:' , balance * 5.10 - chek , 'KT/' ,(balance * 5.10 - chek) / 5.10 , '(SOM)')
