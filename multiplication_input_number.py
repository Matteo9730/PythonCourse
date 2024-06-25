#ask the user to enter a number and print the multiplication table for that number, using a while loop

num = int(input("Inserisci un numero: "))
first = 1

while first <= num:
    print(first * num)
    first += 1