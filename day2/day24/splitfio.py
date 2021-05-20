
a = input('Input full name: ')
if "уулу" in a or "кызы" in a:
    s = a.split()
    print(f"last name: {s[0]} {s[1]},  first name: {s[2]}")

else:
    s = a.split()
    print(f"first name: {s[-1]}  last name: {s[0]}")