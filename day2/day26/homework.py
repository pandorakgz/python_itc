# Problem1

# Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. 
# По умолчанию name = Aman, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge, getGroupNumber, 
# setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента, 
# метод getAge нужен для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения 
# данных о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, 
# метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. 
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.



class Student:
    def __init__(self, name, groupNumber,age):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def getName(self):
        print('Student name: ',self.name)
    def getAge(self):
        print('vozrast Studenta: ',self.age)
    def setgrupName(self):
        print('Gruppa vashego studenta: ', self.groupNumber)
    def setNameAge(self,age):
        self.age = age
        print(self.age)

    def setGroupNumber(self,groupNumber):
        self.groupNumber = groupNumber
        print(self.groupNumber)


zaka = Student(
    name = 'Zalkarbek',
    groupNumber = '11b',
    age = '18'
)
aibek=Student(
    name = 'aibek',
    groupNumber = '21b',
    age = '18'
)

bek=Student(
    name = 'Bektur',
    groupNumber = '16c',
    age = '18'
)

nur=Student(
    name = 'Nurbek',
    groupNumber = '14v',
    age = '18'
)

aigul=Student(
    name = 'Aigul',
    groupNumber = '8b',
    age = '18'
)