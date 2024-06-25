from articolo import Articolo

class Magazzino:
    def __init__(self):
        self._inventario = {}
        
    def getInventario(self):
        return self._inventario
    
    def aggiungi_prodotto(self, codice, descrizione, quantita, scorta=5):
        if codice in self._inventario:
            print(f"Il prodotto {codice} è già presente in magazzino")
        else:
            self._inventario[codice] = Articolo(codice, descrizione, quantita, scorta)
            print(self._inventario[codice].disponibile())

    def sotto_scorta(self):
        sotto_scorta_lista = []
        for codice, articolo in self._inventario.items():
            if articolo.getQuantita() < articolo.getScorta():
                quantita_necessaria = articolo.getScorta() - articolo.getQuantita()
                sotto_scorta_lista.append((articolo, quantita_necessaria))
        return sotto_scorta_lista

    def vendi_articolo(self, codice, quantita):
        articolo = self._inventario.get(codice)
        if articolo:
            return articolo.vendi_articolo(quantita)
        else:
            return f"Articolo {codice} non presente in magazzino."