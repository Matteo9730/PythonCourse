from car import Car

def testCar():  # Creating an instance of Car
    tank_capacity = float(input("Enter the tank capacity in liters: "))
    mileage = float(input("Enter the car's mileage in km/liter: "))
    myCar = Car(mileage, tank_capacity)

    while True:
        print("What do you want to do?")
        print("1. Add fuel")
        print("2. Drive")
        print("3. Check fuel level")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            fuel_added = float(input("How many liters of fuel do you want to add? "))
            myCar.addFuel(fuel_added)
        elif choice == "2":
            distance = float(input("How many kilometers do you want to drive? "))
            myCar.drive(distance)
        elif choice == "3":
            print("The fuel level in the tank is: ", myCar.getFuel(), "liters")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

testCar()

