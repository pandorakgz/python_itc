# # a0 = 1
# # a1 = 2
# # a2 = 3
# # a3 = 4
# # for a in range(11):
# #     print(3,'*',a,'=',a * 3)
# summa = 0
# for a in range(5):
#     summa = summa + a
# print(summa)

mesto = {'darhan', 'Manas - ata', 'Palvan - Ata', 'karavan', 'Baaryna koshulam', 'Offis', 'Faiza'}
meats = {'ash', 'Pizza', 'Pirojok', 'achuu et', 'Lagman', 'Myasnoi rulet', 'Tashhkent ash', 'shashlyk', 'Steik', 'Tibbon'}
jer = mesto.pop()
tamak = meats.pop()

for i in range(3):
    print(i + 1, 'jer',mesto.pop())
    print(i + 1, 'tamak', meats.pop())
    