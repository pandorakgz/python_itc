class AviaSale:
    def __init__(self):
        self.tickets = {
            'Moskva': {
                'data': '20.01.2021',
                'price': 20000
            },
            'Dubai':{
                'data': '20.01.2021',
                'price': 50000
            }
        }

    def get_biletter(self,kud):
        if kud in self.tickets:
            print('bilet','\n',
            'В',kud,'\n',
            'Дата: ',self.tickets[kud]['data'],'\n',
            'Цена: ',self.tickets[kud]['price'])
        else:
            print('bilet na',kud,'net')



samturaAvia = AviaSale()

mesto = input('Куда хотите поехать?: ')
mesto1 = input('От куда хотите поехать?: ')

samturaAvia.get_biletter(mesto)

