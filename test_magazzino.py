from articolo import Articolo
from magazzino import Magazzino
from maxcaratteri import Maxcaratteri

def test_magazzino():
    print("Benvenuto! Il magazzino è ancora vuoto")
    
    try:    #Codice del primo articolo
        codice1 = input("Inserisci prima di tutto il codice dell'articolo. Deve contenere al massimo 12 caratteri: ")
        if len(codice1) > 12:
            raise Maxcaratteri
    except Maxcaratteri as e:
        print(e)
    
    try:    #Descrizione del primo articolo
        descrizione1 = input("Poi inserisci una descrizione dell'articolo, non oltre 50 caratteri: ")
        if len(descrizione1) > 50:
            raise Maxcaratteri
    except Maxcaratteri as e:
        print(e)
    
    try:
        quantita1 = int(input("Specifica la quantità: "))
    except ValueError:
        print("Errore, inserisci numeri interi")
    
    magazzino = Magazzino()
    magazzino.aggiungi_prodotto(codice1, descrizione1, quantita1)
    
    while True:
        print("Cosa vuoi fare?")
        print("1. Effettua un ordine di un articolo")
        print("2. Vendi un articolo")
        print("3. Aggiungi un nuovo articolo")
        print("4. Esci")

        
        scelta = input("Inserisci la tua scelta: ")

        if scelta == "1":
            codice = input("Inserisci il codice dell'articolo da acquistare: ")
            quantita = int(input("Inserisci la quantità da acquistare: "))
            articolo = magazzino.getInventario().get(codice)
            if articolo:
                print(articolo.acquisto(quantita))
            else:
                print(f"Articolo {codice} non presente in magazzino.")
        elif scelta == "2":
            codice = input("Inserisci il codice dell'articolo da vendere: ")
            quantita = int(input("Inserisci la quantità da vendere: "))
            articolo = magazzino.getInventario().get(codice)
            if articolo:
                print(articolo.vendi_articolo(quantita))
            else:
                print(f"Articolo {codice} non presente in magazzino.")
        elif scelta == "3":
            try:
                codice = input("Inserisci il codice del nuovo articolo: ")
                if len(codice) > 12:
                    raise Maxcaratteri
            except Maxcaratteri as e:
                print(e)
                    
            try:
                descrizione = input("Inserisci una descrizione del nuovo articolo: ")
                if len(descrizione) > 50:
                    raise Maxcaratteri
            except Maxcaratteri as e:
                print(e)
                    
            try:
                quantita = int(input("Inserisci la quantità iniziale del nuovo articolo: "))
            except ValueError:
                print("Errore, inserisci numeri interi")
                    
                magazzino.aggiungi_prodotto(codice, descrizione, quantita)

        elif scelta == "4":
            print("Grazie e arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")
test_magazzino()