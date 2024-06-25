from benzina import Benzina
from diesel import Diesel
from optional import Optional


auto1 = Benzina("evfvrv", "Honda", "modello1", 1234, 4)

codice = "abc"
descrizione = "Bellissimoooo"
valore = 20
optional1 = ([codice, descrizione, valore])

auto1 = Optional("evfvrv", "Honda", "modello1", optional1)

print(auto1.stampa())
print(auto1.stampa_optional())



'''
codice = "abc"
descrizione = "Bellissimoooo"
valore = 20
optional1 = codice, descrizione, valore
auto1 = Optional("evfvrv", "Honda", "modello1", optional1)
auto1.aggiungi_optional(optional1)
codice2 = "ciao"
descrizione2 = "Fa schifo"
valore2 = 1
optional2 = ([codice2, descrizione2, valore2])
auto1.aggiungi_optional(codice2)
print(auto1.stampa())
print(auto1.stampa())
'''