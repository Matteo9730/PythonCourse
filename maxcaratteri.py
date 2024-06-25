class Maxcaratteri(Exception):
    def __init__(self, message= "Errore, ci sono troppi caratteri"):
        self.message= message
        super().__init__(self.message)