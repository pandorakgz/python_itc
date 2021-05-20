import random
class Bank:
    def __init__(self, bank_name, bank_balance):
        self.bank_name = bank_name
        self.bank_balance = bank_balance

    def bank_info(self):
        print('Добро пожаловать: ', self.bank_name)

    # открытие счета
    def create_account(self, client_name, password):
        rnd = random.randint(1000,2000)
        self.client_name = client_name
        self.password = password
        self.accaunts = {
            rnd: {
                'name': client_name,
                'password': password,
                'balance':0
            }
        }
        print('vash akkaunt otkryt:','\n',
        'name: ', self.accaunts[rnd]['name'],'\n',
        'password: ', self.accaunts[rnd]['password'],'\n',
        'balance: ', self.accaunts[rnd]['balance'],'\n'
        )
        print('schet vashego akkaunta:',rnd)
        return rnd

        
    # оборот банка
    def get_bank_balance(self):
        print('Balans banka',self.bank_balance)
    
    # данные о счете
    def get_account(self, nomer):
        print('vash schet:','\n',
        'name: ', self.accaunts[nomer]['name'],'\n',
        'password: ', self.accaunts[nomer]['password'],'\n',
        'balance: ', self.accaunts[nomer]['balance'],'\n')

    # получаем баланс на счете
    def get_balance(self, nomer):
        print('Dengi na vashem schetu:',
        self.accaunts[nomer]['balance']
        )
    
    def add_money_to_balance(self,nomer, money):
        self.accaunts[nomer]['balance']=self.accaunts[nomer]['balance']+money
        print('vashi dengi uvelichelis na', money)

    # создаем электронную карту
    def create_card(self, client_name, type, password):
        self.client_name = client_name
        self.type = type
        self.password = password
    
    # получаем карты клиента
    def get_credits_card(self, client_name):
        self.client_name = client_name
