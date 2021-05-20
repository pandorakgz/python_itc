# class Animal:
#     def __init__(self, name, speed,massa,hp,attack):
#         self.name = name
#         self.speed = speed
#         self.massa = massa
#         self.hp = hp
#         self.attack = attack
#     def attack_foot(self):
#         print(self.name, 'общая атака attack foot 30')
        

# class Lion(Animal):
#     def attack_1(self):
#         print(self.name, 'атака: ', self.attack)

# class KingKong(Animal):
#     def attack_1(self):
#         print(self.name, 'атака: ', self.attack)

# class Krokodile(Animal):
#     def attack_1(self):
#          print(self.name, 'атака: ', self.attack)

# tigr = Lion(
#     name = 'Sherkhan',
#     speed = 15,
#     massa = 50,
#     hp = 100,
#     attack = 20
# )

# mankey = KingKong(
#     name = 'Tank',
#     speed = 10,
#     massa = 100,
#     hp = 110,
#     attack = 30
# )

# ryba = Krokodile(
#     name = 'Gena',
#     speed = 20,
#     massa = 50,
#     hp = 105,
#     attack = 19
# )

# tigr.attack_1()
# mankey.attack_1()
# ryba.attack_1()
# tigr.attack_foot()
# mankey.attack_foot()
# ryba.attack_foot()




class Animal:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Lion(Animal):
    def to_attack(self):
        print(self.name,':','Roar', 'Tackle')
        print('health: ', self.hp)

class KingKong(Animal):
    def to_attack(self):
        print(self.name,':','Hyper Punch','Tackle')
        print('health: ', self.hp)


class Krokodile(Animal):
    def to_attack(self):
        print(self.name,':','Earthquake','Tackle')
        print('health: ', self.hp)
animal  = Animal('leo',55)

leo = Lion(
    name='leo',
    hp=130
)
kingkong = KingKong(
    name='kingkong',
    hp=630

)    
krok = Krokodile(
    name='krok',
    hp=55
)


kingkong.to_attack()
leo.to_attack()
krok.to_attack()