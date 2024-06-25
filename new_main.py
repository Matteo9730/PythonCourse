from new_bank_account import BankAccount
from new_error import Zero


def main():
    account = BankAccount()
    print("You have 0 euros in your account.")

    while True:
        print("\nWhat would you like to do with your account?")
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. Check balance")
        print("4. View last 5 transactions")
        print("5. Exit")

        while True:
            try:
                choice = int(input("Your choice: "))
                if choice not in range(1, 6):
                    raise ValueError
                break
            except ValueError:
                print("Please choose a number from 1 to 5.")

        if choice == 1:
            try:
                deposit_amount = float(input("How much would you like to deposit? "))
                if deposit_amount <= 0:
                    raise Zero
                print(account.deposit(deposit_amount))
            except ValueError:
                print("The amount must be a number.")
            except Zero as e:
                print(e)

        elif choice == 2:
            try:
                withdrawal_amount = float(input("How much would you like to withdraw? "))
                if withdrawal_amount <= 0:
                    raise Zero
                print(account.withdraw(withdrawal_amount))
            except ValueError:
                print("The amount must be a number.")
            except Zero as e:
                print(e)

        elif choice == 3:
            print("Here is your balance:")
            print(f"{account.getBalance()} euros")

        elif choice == 4:
            account.show_last_five_transactions()

        elif choice == 5:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()