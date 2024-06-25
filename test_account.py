from bank_account import BankAccount

def main():
    """
    Main function to test the BankAccount class.
    """
    print("The account is empty, please make a deposit to use it.")
    initial_deposit = float(input("How much do you want to deposit? "))
    account = BankAccount(initial_deposit)

    while True:
        print(f"You have {account.getBalance()} euros in your account, what do you want to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Recent Transactions")
        print("5. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            amount = float(input("How much do you want to deposit? "))
            account.deposit(amount)
            print(f"You have just deposited {amount} euros, your new balance is {account.getBalance()} euros.")

        elif choice == "2":
            amount = float(input("How much do you want to withdraw? "))
            account.withdraw(amount)
            print(f"You have just withdrawn {amount} euros, your new balance is {account.getBalance()} euros.")

        elif choice == "3":
            print(f"Your account balance is: {account.getBalance()} euros.")

        elif choice == "4":
            transactions = account.recent_transactions()
            if transactions:
                print("The last 5 transactions:")
                for transaction in transactions:
                    print(transaction)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()