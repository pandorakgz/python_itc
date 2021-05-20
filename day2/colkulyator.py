n = int(input('1 chislo: '))
b = int(input('2 chislo: '))

s = input('kandai amal: ')

if s == '+':
    print(n + b)

if s == '-':
    print(n - b)

if s == '*':
    print(n * b)

if s == '/' and n != 0:

    print(n / b)
else:
    print('На ноль делить нельзя:')
    

if s == '**':
    print(n ** b)





# s = int(input('Введите число: '))

# if 1 == s:
#   print('понедельник')
# elif 2 == s:
#   print('вторник')
# elif 3 == s:
#   print('среда')
# elif 4 == s:
#   print('четверг')
# elif 5 == s:
#   print('пятница')
# elif 6 == s:
#   print('суббота')
# elif 7 == s:
#   print('воскресенье')
# else:
#   print('не гони')