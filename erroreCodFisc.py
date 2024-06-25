class erroreCodFisc(Exception):
    def __init__(self, message= "Errore, hai sbagliato il codice fiscale"):
        self.message= message
        super().__init__(self.message)