#concatenate all characters of a string into a new string without vowels, with a for loop

string = input("Enter a string: ")
tot = ""
for i in string:
    if i in ("aeiouAEIOU"):
        pass
    else:
        tot += i
print(tot)