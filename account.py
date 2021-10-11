class Account:

    def __init__(self, number, owner, balance1, limit):
        print("Building object ... {}".format(self))
        self.__number = number
        self.__owner = owner
        self.__balance1 = balance1
        self.__limit = limit

    def balance(self):
        print('Account owner: {}\nUpdated balance: €{:.2f}.'.format(self.__owner, self.__balance1))

    def deposit(self, value):
        self.__balance1 += value

    def __can_withdraw(self, value_to_withdraw):
        available_vale = self.__balance1 + self.__limit
        return value_to_withdraw <= available_vale
        pass

    def withdraw(self, value):
        if self.__can_withdraw(value):
            self.__balance1 -= value
        else:
            print("The value {} is bigger than your limit".format(value))

    def transfer(self, valor, destination):
        self.withdraw(valor)
        destination.deposit(valor)

    @property
    def balance1(self):
        return self.__balance1

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return {'AIB': '001', 'BOI': '231', 'Revolut': '333'}
