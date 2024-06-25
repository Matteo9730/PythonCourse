from new_tank import Tank

print("Enter the tank capacity: ")
while True:
    try:
        capacity = int(input(""))
        break
    except ValueError:
        print("It must be a number")

tank = Tank(capacity)

while True:
    print("What would you like to do?")
    print("1. Check the liquid level")
    print("2. Refill the tank")
    print("3. Use the tank")
    print("4. Exit")

    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("It must be a number from 1 to 4")

    if choice == 1:
        print(f"The current level is {tank.getLevel()}")
    elif choice == 2:
        print("How much would you like to refill?")
        while True:
            try:
                refill_amount = int(input(""))
                break
            except ValueError:
                print("It must be a number")
        print(tank.refill(refill_amount))
        print(f"The current level is now {tank.getLevel()}")
    elif choice == 3:
        print("How much would you like to consume?")
        while True:
            try:
                consume_amount = int(input(""))
                break
            except ValueError:
                print("It must be a number")
        print(tank.consume(consume_amount))
        print(f"The current level is now {tank.getLevel()}")
    elif choice == 4:
        print("Goodbye")
        break
    else:
        print("Invalid choice")
