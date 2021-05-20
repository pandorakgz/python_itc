

class Klient:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.set_password(password)

    def set_password(self, password):
        if len(password) < 7:
            print('Пароль слабый')
        elif len(password) >= 8:
            self.__password = password

    def get_password(self):
        return 'шифрованный'

    def raw_password(self):
        print('Ни каму не рассказывай пароль')
        return self.__password



turgun = Klient('Turgunbai', 'turgun', '19947712')
# print(turgun.login)
# turgun.set_password('12000000003')
# print(turgun.get_password())
# print(turgun.raw_password())
