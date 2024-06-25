'''
Creare una classe di nome Persona con le variabili di istanza: cognome, nome, codice fiscale e città di tipo stringa.
La classe deve contenere un costruttore parametrico; i metodi set e
get ed un metodo chiamato annoNascita che a partire dal codice fiscale ricavi e restituisca l'anno di nascita di una persona.
Creare un'applicazione che istanzi un oggetto della classe Persona e ne visualizzi in seguito nome, cognome ed anno di nascita
'''
from persona import Persona
from stagista import Stagista
from erroreCodFisc import erroreCodFisc

def test_persona():
    nome1 = input("Come si chiama la prima persona? ")
    cognome1 = input("Ora dirmi il cognome: ")
    while True:
        try:
            codiceFisc1 = input("Ora il codice fiscale: ")
            if len(codiceFisc1) < 12:
                raise erroreCodFisc
        except erroreCodFisc as e:
            print(e)
        break
    citta1 = input("La città: ")
    while True:
        try:
            numeropresenze1 = int(input("Quante ore di presenze ha? "))
            numeroidentificativo1 = int(input("Infine, il suo numero identificativo: "))
        except ValueError:
            print("Deve essere un numero.")
        break
    persona1 = Stagista(cognome1, nome1, codiceFisc1, citta1, numeropresenze1, numeroidentificativo1)
    print(persona1.stampa())
    
    nome2 = input("Come si chiama la seconda persona? ")
    cognome2 = input("Ora dirmi il cognome: ")
    while True:
        try:
            codiceFisc2 = input("Ora il codice fiscale: ")
            if len(codiceFisc2) < 12:
                raise erroreCodFisc
        except erroreCodFisc as e:
            print(e)
        break
    citta2 = input("La città: ")
    while True:
        try:
            numeropresenze2 = int(input("Quante ore di presenze ha? "))
            numeroidentificativo2 = int(input("Infine, il suo numero identificativo: "))
        except ValueError:
            print("Deve essere un numero.")
        break
    persona2 = Stagista(cognome2, nome2, codiceFisc2, citta2, numeropresenze2, numeroidentificativo2)

    nome3 = input("Come si chiama la terza persona? ")
    cognome3 = input("Ora dirmi il cognome: ")
    while True:
        try:
            codiceFisc3 = input("Ora il codice fiscale: ")
            if len(codiceFisc3) < 12:
                raise erroreCodFisc
        except erroreCodFisc as e:
            print(e)
        break
    citta3 = input("La città: ")
    while True:
        try:
            numeropresenze3 = int(input("Quante ore di presenze ha? "))
            numeroidentificativo3 = int(input("Infine, il suo numero identificativo: "))
        except ValueError:
            print("Deve essere un numero.")
        break
    persona3 = Stagista(cognome3, nome3, codiceFisc3, citta3, numeropresenze3, numeroidentificativo3)
    
    stagisti = [persona1, persona2, persona3]
    
    giovane = max(stagisti, key = lambda x: x.annoNascita())
    
    print("Informazioni dello stagista più giovane: ")
    print(f"Cognome: {giovane.getCognome()}, nome: {giovane.getNome()}, codice fiscale: {giovane.getCodiceFisc()}, Il suo anno di nascita: {giovane.annoNascita()}, dove vive: {giovane.getCitta()}, il suo numero di presenze: {giovane.getNumeropresenze()} e il suo numero identificativo: {giovane.getNumeroidentificativo()}")
   
   
test_persona()