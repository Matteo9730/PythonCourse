from Auto import Auto

class Optional(Auto):
    def __init__(self, targa, marca, modello, codice = []):
        super().__init__(targa, marca, modello)
        self.__codice = codice
        
    def aggiungi_optional(self, codice):
        self.__codice.append(codice)

    def stampa(self):
        pass
        
    def stampa_optional(self):
        return f"{self.__codice}"
    