from motore import Motore

class Diesel(Motore):
    def __init__(self, targa, marca, modello, cilindrata, cilindri):
        super().__init__(targa, marca, modello)
        self.__setCilindrata(cilindrata)
        self.__setCilindri(cilindri)
        
    def __setCilindrata(self, cilindrata):
        self.__cilindrata = cilindrata
    def getCilindrata(self):
        return self.__cilindrata
    
    def __setCilindri(self, cilindri):
        self.__cilindri = cilindri
    def getCilindri(self):
        return self.__cilindri
    
    def potenza(self):
        return self.getCilindrata() * self.getCilindri() * 1.5

    def rpm_massimi(self):
        return 6000
    
    def stampa(self):
        return f"{super().info_generiche()}; Potenza: {self.potenza()}, rpm massimi: {self.rpm_massimi()}"
    
    def stampa_optional(self):
        pass


    
