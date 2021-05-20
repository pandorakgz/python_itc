# Задача 1.
# создайте файл friends.txt
# напишите туда имена своих друзей и их возраст с помощью open('friends.txt', 'w')
# Например содержимое файла должен быть:
    # Руслан,26
    # Кадыр,23
    # Ерлан,22

# frend = {
#     'aibek' : 2002,
#     'nurbek' : 2001,
#     'kylym' : 2002,
#     'nurbolot' : 2001
# }


# frend_file = open('friend.txt','w')
# for key, value in frend.items():
#     print(key,value)
#     frend_file.writelines(key+':'+str(value)+',''\n')

# except FileNotFoundError:
#     print('takoy faila  netu')
# except NameError:
#     print('Nepravilnye peremennye ')
# except ValueError:
#     print('oshibka vedite chislo a ne tekst ')
# except ZeroDivisionError:
#     print('Oshibka na noli deliti nrelizy ')
# except TypeError:
#     print('oshipka tipa ')


# Задание 2
# Создайте функцию splitFio(fio) которое разделяет имя и фамилию
# Например:
    # Ввод: splitFio('Асан уулу Рулсан')
    # Вывод: Имя: Руслан Фамилия: Асан уулу
    
    # Ввод: splitFio('Тургунбаева Айсулуу')
    # Вывод: Имя: Айсулуу Фамилия: Тургунбаева

# a = input('Input full name: ')
# if "уулу" in a or "кызы" in a:
#     s = a.split()
#     print(f"last name: {s[0]} {s[1]},  first name: {s[2]}")

# else:
#     s = a.split()
#     print(f"first name: {s[-1]}  last name: {s[0]}")

# Задание 3
# создайте файл tasks.txt и напишите туда разные уравнения
# создайте функцию run_task() которое открывает файл tasks.txt и выполняет уравнения
# Например содержимое файла tasks.txt:
# 20+99
# 199/3
# 200**5
# 500+1976
# При запуске функции run_task()
# Вывод:
#   20+99=119
#   199/3=106
#   200**5=320000000000
#   500+1976=2476



run_task = open('friend.txt','r')
run_task1 = run_task.readlines()

for task in run_task1:
    try:
        t = task.strip()
        print(t,'=', eval(t))
    except FileNotFoundError:
        print('takoy faila  netu')
    except NameError:
        print('Nepravilnye peremennye ')
    except ValueError:
        print('oshibka vedite chislo a ne tekst ')
    except ZeroDivisionError:
        print('Oshibka na noli deliti nrelizy ')
    except TypeError:
        print('oshipka tipa ')