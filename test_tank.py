from tank import Tank


def testTank():
    try:
        tank_capacity = int(input("Enter the tank capacity in liters: "))
        tank = Tank(tank_capacity)

        while True:

            print("The current tank level is: ", tank.getLevel(), " liters")
            print("What would you like to do?")
            print("1. Use a certain amount of liquid from the tank")
            print("2. Refill the tank")
            print("3. Exit")

            choice = input("Choice: ")

            if choice == "1":
                amount = int(input("How many liters do you want to use? "))
                tank.consume(amount)
            elif choice == "2":
                amount = int(input("How much do you want to refill? "))
                tank.refill(amount)
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again!")
    except ValueError:
        print("You should enter a number")


testTank()
