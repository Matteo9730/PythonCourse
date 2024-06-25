class Tank:
    def __init__(self, capacity):
        self.__setCapacity(capacity)
        self.__setLevel(0)  # Initialize the level to 0

    def __setCapacity(self, capacity):  # Set the capacity attribute
        self.__capacity = capacity

    def __setLevel(self, level):  # Set the water level and check it doesn't go below 0
        if level < 0:
            print("The tank is empty")
        else:
            self.__level = level

    def getLevel(self):  # Returns the current level
        return self.__level

    def consume(self, amount):
        if self.getLevel() >= amount:
            self.__setLevel(self.getLevel() - amount)
        else:
            print("You have emptied the tank, refill it!")

    def refill(self, amount):
        if amount > self.__capacity and amount > self.getLevel():
            print("Tank is full")
        else:
            self.__setLevel(self.getLevel() + amount)
    
    
    
    