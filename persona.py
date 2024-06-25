'''
Creare una classe di nome Persona con le variabili di istanza: cognome, nome, codice fiscale e città di tipo stringa.
La classe deve contenere un costruttore parametrico; i metodi set e
get ed un metodo chiamato annoNascita che a partire dal codice fiscale ricavi e restituisca l'anno di nascita di una persona.
'''
import datetime

class Persona:
    def __init__(self, cognome, nome, codiceFisc, citta):
        self.__setCognome(cognome)
        self.__setNome(nome)
        self.__setCodiceFisc(codiceFisc)
        self.__setCitta(citta)
    
    def __setCognome(self, cognome):
        self.__cognome = cognome
    def getCognome(self):
        return self.__cognome
        
    def __setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    
    def __setCodiceFisc(self, codiceFisc):
        self.__codiceFisc = codiceFisc
    def getCodiceFisc(self):
        return self.__codiceFisc
        
    def __setCitta(self, citta):
        self.__citta = citta
    def getCitta(self):
        return self.__citta
        
    def annoNascita(self):
        if int(self.getCodiceFisc()[6]) >= 3:
            data = "19" + self.getCodiceFisc()[6:8]
            anno = int(data)
            return f"{anno}"
        elif (int(self.getCodiceFisc()[6]) <= 2) and (int(self.getCodiceFisc()[7]) < 5):
            data = "20" + self.getCodiceFisc()[6:8]
            anno = int(data)
            return f"{anno}"
        else:
            return f"Errore"
    
    def stampa(self):
        return f"{self.getNome()}, {self.getCognome()}, {self.annoNascita()}"