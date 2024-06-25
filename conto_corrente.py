class ContoBancario:
    def __init__ (self, numero, bilancio = 0, fido = 0):
        self.__setNumero(numero)
        self.__setBilancio(bilancio)
        self.setFido(fido)
        
    def __setNumero(self, numero):
        self.__numero = numero
    def getNumero(self):
        return self.__numero
    
    def __setBilancio(self, bilancio):
        self.__bilancio = bilancio
    def getBilancio(self):
        return self.__bilancio
   
    def deposita(self, importo):
        self.__setBilancio(self.getBilancio() + importo)
        print(f"Hai appena versato {importo} euro, ti rimangono {self.getBilancio()} euro.")
        
    def setFido(self, fido):
        self.__fido = fido
    def getFido(self):
        return self.__fido
    
    def preleva(self, importo):
        differenza = self.getBilancio() - (importo + self.getFido())
        if importo <= differenza:
            nuovo_bilancio = self.getBilancio() - importo
            self.__setBilancio(nuovo_bilancio)
            print(f"Hai appena prelevato {importo} euro dal conto, ti rimangono {self.getBilancio()} euro. ")
        else:
            print("Non hai abbastanza soldi nel conto")
    