#count the number of vowels in a string

string = input("Enter a string: ")
tot = 0
for i in string:
    if i in ("aeiouAEIOU"):
        tot += 1
    else:
        pass
print(tot)