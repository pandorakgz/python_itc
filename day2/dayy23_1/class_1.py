class Person:
    def __init__(self, name = 'Нету', age=0):
        self.name = name
        self.__age = age
    def set_age(self,age):
        if age > 100:
            print('Недопустимый возраст')
        else:
            self.__age = age
    def get_age(self):
        if self.__age == 0:
            return'vy ne vveli vozrast'
        else:
            return self.__age




me = Person(name = 'Zalkarbek',age = 34)

print(me.get_age())