#write a function that takes a string as a input ansd returns the string with the characters inverted

string = input("Scrivi qualcosa: ")

def function(x):
    string1 = ""
    for y in x:
        string1 = y + string1
    print(string1)

function(string)