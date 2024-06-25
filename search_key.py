#write a function that takes a dictionary and a key as input and returns the value associated with that key, if present

dictionary= {
 "brand": "Ford",
 "modello": "Mustang",
 "anno": 1964
}

key = input("Search something in the dictionary: ")

def funzione(x,y):
    if y in x:
        print(x[y])
    else:
        print("There's not")

funzione(dictionary, key)