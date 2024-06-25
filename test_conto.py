from conto_corrente import ContoBancario
import random

def cc():
    print("Il conto è vuoto, per usufruire effettua un versamento")
    inizio= float(input("Quanto vuoi versare? "))
    numero_conto = random.randint(1000, 10000)
    conto = ContoBancario(numero_conto, inizio)
    
    while True:
        print(f"Hai {conto.getBilancio()} euro sul conto, cosa vuoi fare?") 
        print("1. Versamenti")
        print("2. Prelievi")
        print("3. Saldo")
        print("4. Effettuare un fido")
        print("5. Uscire")
        
        scelta = input("Scelta: ")
        if scelta == "1":
            i = float(input("Quanto vuoi versare? "))
            conto.deposita(i)
        
        elif scelta == "2":
            k = float(input("Quanto vuoi prelevare? "))
            conto.preleva(k)
        
        elif scelta == "3":
            print(f"Il saldo del conto: {conto.getBilancio()} euro.")
        
        elif scelta == "4":
            fido1= float(input("Di quant è il fido? "))
            conto.setFido(fido1)
            while True:
                print(f"Hai {conto.getBilancio()} euro sul conto, cosa vuoi fare?") 
                print("1. Versamenti")
                print("2. Prelievi")
                print("3. Saldo")
                print("4. Uscire")
        
                scelta = input("Scelta: ")
                if scelta == "1":
                    i = float(input("Quanto vuoi versare? "))
                    conto.deposita(i)
        
                elif scelta == "2":
                    k = float(input("Quanto vuoi prelevare? "))
                    conto.preleva(k)
        
                elif scelta == "3":
                    print(f"Il saldo del conto: {conto.getBilancio()} euro.")
        
                elif scelta == "4":
                    print("Arrivederci!")
                    break
                else:
                    print("Scelta non valida. Riprova!")
            break
                
        elif scelta == "5":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova!")


cc()