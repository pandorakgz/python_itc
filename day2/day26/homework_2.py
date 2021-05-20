# Problem2

# Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы addition — сложение, 
# multiplication — умножение, division — деление, subtraction — вычитание. 
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class myMath:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        print('a + b = ', self.a + self.b )

    def addition(self):
        print('a - b = ', self.a - self.b )

    def addition(self):
        print('a ** b = ', self.a ** self.b )
    
    def addition(self):
        print('a / b = ', self.a / self.b )
# a = int(input(': '))
# b = int(input(': '))
primer = myMath(a = 5, b = 8)
primer.addition()