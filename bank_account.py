class BankAccount:
    def __init__(self, balance: float):
        self.__setBalance(balance)
        self.__transactions = []

    def __setBalance(self, balance: float):
        """
        Set the account balance, ensuring it is not negative.
        """
        if balance <= 0:
            print("Your account is empty, make a deposit!")
        else:
            self.__balance = balance

    def getBalance(self) -> float:
        """
        Return the account balance.
        """
        return self.__balance

    def withdraw(self, amount: float):
        """
        Withdraw money from the account if sufficient balance is available.
        """
        if self.getBalance() >= amount:
            self.__setBalance(self.getBalance() - amount)
            self.__transactions.append(f"Withdrawal of {amount} euros.")
        else:
            print("Insufficient funds in the account.")

    def deposit(self, amount: float):
        """
        Deposit money into the account.
        """
        self.__setBalance(self.getBalance() + amount)
        self.__transactions.append(f"Deposit of {amount} euros.")

    def recent_transactions(self):
        """
        Return the last 5 transactions, if available.
        """
        if len(self.__transactions) > 5:
            return self.__transactions[-5:]
        elif len(self.__transactions) >= 1:
            return self.__transactions
        else:
            print("No transactions found.")
            return []