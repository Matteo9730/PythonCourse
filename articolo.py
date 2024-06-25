'''
Si progetti e realizzi un'applicazione che dato un magazzino di articoli di cui si conosce:
Codice (massimo 12 caratteri)
Descrizione (massimo 50 caratteri)
Quantità in magazzino
Quantità sotto scorta
Si permetta la creazione di articoli senza specificare il sotto scorta
Dietro richiesta del magazzino calcoli se l'articolo deve essere ordinato al fornitore e in quale quantità minima
In caso di ordine da cliente il magazzino controlla se l'articolo è disponibile e in caso negativo segnali la quantità da ordinare 
per eseguire l'ordine
In caso di acquisto da un fornitore, inserire la quantità acquistata
'''
class Articolo:
    def __init__(self, codice, descrizione, quantita, scorta=5):
        self.__setCodice(codice)
        self.__setDescrizione(descrizione)
        self.__setQuantita(quantita)
        self.scorta = scorta
        
    def getCodice(self):
        return self._codice
    
    def __setCodice(self, codice):
        self._codice = codice
        
    def getDescrizione(self):
        return self._descrizione
    
    def __setDescrizione(self, descrizione):
        self._descrizione = descrizione
        
    def getQuantita(self):
        return self._quantita
    
    def __setQuantita(self, quantita):
        self._quantita = quantita
    
    def disponibile(self):
        if self._quantita > self.scorta:
            return f"Sono presenti {self._quantita} pezzi"
        elif self._quantita > 0:
            return "Occhio! Sei sotto scorta."
        else:
            return "L'articolo al momento non è presente."
    
    def acquisto(self, aggiunta):
        self._quantita += aggiunta
        return f"Sono stati aggiunti {aggiunta} pezzi al prodotto {self.codice}"
    
    def vendi_articolo(self, quantita):
        if self._quantita >= quantita and quantita > 0:
            self._quantita -= quantita
            return f"Articolo {self.codice} venduto con successo. Quantità rimanente: {self._quantita}"
        elif quantita < 0:
            self._quantita -= quantita  # Vendita negativa equivale ad acquisto
            return f"Articolo {self.codice} acquistato con successo. Nuova quantità: {self._quantita}"
        elif self._quantita < quantita:
            quantita_necessaria = quantita - self._quantita
            return f"Articolo {self.codice} non disponibile. Quantità necessaria: {quantita_necessaria}"
        else:
            return "Quantità non valida"
