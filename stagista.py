from persona import Persona

class Stagista(Persona):
    def __init__(self, cognome, nome, codiceFisc, citta, numeropresenze, numeroidentificativo):
        super().__init__(cognome, nome, codiceFisc, citta)
        self.__setNumeropresenze(numeropresenze)
        self.__setNumeroidentificativo(numeroidentificativo)
    
    def __setNumeropresenze(self, numeropresenze):
        self.__numeropresenze = numeropresenze
    def getNumeropresenze(self):
        return self.__numeropresenze
    
    def __setNumeroidentificativo(self, numeroidentificativo):
        self.__numeroidentificativo = numeroidentificativo
    def getNumeroidentificativo(self):
        return self.__numeroidentificativo
    
        