class Tank:
    def __init__(self, capacity):
        self.setCapacity(capacity)
        self.setLevel(0)

    def setCapacity(self, capacity):
        self.__capacity = capacity

    def getCapacity(self):
        return self.__capacity

    def setLevel(self, level):
        self.__level = level

    def getLevel(self):
        return self.__level

    def refill(self, liters):
        difference = self.getCapacity() - self.getLevel()
        if self.getCapacity() < self.getLevel() + liters:
            self.setLevel(self.getLevel() + difference)
            return f"Too many liters for the capacity, {difference} liters have been added"
        else:
            self.setLevel(self.getLevel() + liters)
            return f"{liters} liters have been added"

    def consume(self, liters):
        if self.getLevel() < liters:
            difference = self.getLevel()
            self.setLevel(0)
            return f"Too many liters compared to the level, you have consumed {difference} liters. Now it's at 0"
        else:
            self.setLevel(self.getLevel() - liters)
            return f"You have consumed {liters} liters"