from account import Account

account1 = Account(123, "Renato", 55, 1000.0)
account2 = Account(321, "Bruna", 67, 1000.0)

print(account1.balance())
print(account2.balance())

print("_"*20)

account1.withdraw(1200.0)
account1.withdraw(100.0)
print(account1.balance())