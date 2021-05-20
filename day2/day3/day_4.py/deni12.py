def calculator (san1, san2, suff):
    if suff == '*':
        print(san1 * san2)
    elif suff =='/':
        print(san1 / san2)
    elif suff == '-':
        print(san1 - san2)
    elif suff == '+':
        print(san1 + san2)
    elif suff == '**':
        print(san1 ** san2)

n1 = int(input('Сан териниз: '))
n2 = int(input('Сан териниз: '))
s = input('Кандай амал: ')
calculator(n1, n2, s)