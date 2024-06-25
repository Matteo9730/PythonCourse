from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, targa, marca, modello):
        self.__setTarga(targa)
        self.__setMarca(marca)
        self.__setModello(modello)
    
    def __setTarga(self, targa):
        self.__targa = targa
    def getTarga(self):
        return self.__targa
    
    def __setMarca(self, marca):
        self.__marca = marca
    def getMarca(self):
        return self.__marca
    
    def __setModello(self, modello):
        self.__modello = modello
    def getModello(self):
        return self.__modello
    
    def info_generiche(self):
        return f"Targa: {self.getTarga()}; Marca: {self.getMarca()}; Modello: {self.getModello()}"
    
    @abstractmethod
    def stampa(self):
        pass

    @abstractmethod
    def stampa_optional(self):
        pass
    