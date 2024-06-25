class Car:
    def __init__(self, mileage, capacity):  # 2 methods
        self.__setCapacity(capacity)
        self.__setMileage(mileage)  # Calls 3 private methods (__setMileage, __setCapacity, __setFuel)
        self.__setFuel(0)  # to initialize the private attributes (__mileage, __capacity, __fuel)

    def __setMileage(self, mileage):  # Used to set the value of the respective attribute
        self.__mileage = mileage

    def __setCapacity(self, capacity):  # Used to set the value of the respective attribute
        self.__capacity = capacity

    def __setFuel(self, fuel):  # Used to set the value of the respective attribute
        if fuel < 0:
            print("You have no fuel left!")
        else:
            self.__fuel = fuel

    def getFuel(self):  # Tells you how much fuel there is
        return self.__fuel

    def addFuel(self, fuel):  # Allows you to add fuel to the tank
        if fuel > self.__capacity - self.getFuel():
            self.__setCapacity(self.__capacity)
            print("Tank full")
        else:
            self.__setFuel(self.getFuel() + fuel)

    def drive(self, km):  # Simulates driving the car for a certain distance
        consumption = km / self.__mileage
        if self.getFuel() >= consumption:
            self.__setFuel(self.getFuel() - consumption)
            print("Have a good trip!")
        else:
            print("You ran out of fuel, refuel!")
