class BankAccount:
    def __init__(self, balance=0):
        self.__setBalance(balance)
        self.__transactions = []

    def __setBalance(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__setBalance(self.getBalance() + amount)
        self.__transactions.append(f"Deposit of {amount} euros")
        return f"You have deposited {amount} euros into your account."

    def withdraw(self, amount):
        if self.getBalance() < amount:
            return "Insufficient funds."
        else:
            self.__setBalance(self.getBalance() - amount)
            self.__transactions.append(f"Withdrawal of {amount} euros")
            return f"You have withdrawn {amount} euros from your account."

    def show_last_five_transactions(self):
        print("Here are the last 5 transactions:")
        print(self.__transactions[-5:])