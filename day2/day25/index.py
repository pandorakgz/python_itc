import bank1_1
# 1
demir = bank1_1.Bank(
    bank_name = 'Demir Bank',
    bank_balance = 750_000_000.00
)

nomer = demir.create_account(
    client_name= 'Zalkarbek',
    password=1994
)

demir.bank_info()
demir.get_bank_balance()
demir.add_money_to_balance(nomer,11100)
demir.get_account(nomer)

# 2
dos = bank1_1.Bank(
    bank_name = 'Dos Credo',
    bank_balance = 7_000_000.00
)

nomer = dos.create_account(
    client_name= 'Zalkarbek',
    password=2002
)

dos.bank_info()
dos.get_bank_balance()
dos.add_money_to_balance(nomer,224324)
dos.get_account(nomer)

# 3
rsk = bank1_1.Bank(
    bank_name = 'RSK',
    bank_balance = 73_552_000_000.000
)

nomer = rsk.create_account(
    client_name= 'Zalkarbek',
    password=2003
)

rsk.bank_info()
rsk.get_bank_balance()
rsk.add_money_to_balance(nomer,2247334)
rsk.get_account(nomer)

# 4
aiyl = bank1_1.Bank(
    bank_name = 'Айыл банк',
    bank_balance = 7_000_000.00
)

nomer = aiyl.create_account(
    client_name= 'Zalkarbek',
    password=2002
)

aiyl.bank_info()
aiyl.get_bank_balance()
aiyl.add_money_to_balance(nomer,224324)
aiyl.get_account(nomer)

# 5
aman = bank1_1.Bank(
    bank_name = 'Аман Банк',
    bank_balance = 7_000_000.00
)

nomer = aman.create_account(
    client_name= 'Zalkarbek',
    password=2002
)

aman.bank_info()
aman.get_bank_balance()
aman.add_money_to_balance(nomer,224324)
aman.get_account(nomer)
