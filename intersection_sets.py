#write a function that takes two sets as input and returns a set containing the common elements between two sets

set1 = set()
set2 = set()

x = 1
while x <= 4:
    word = input("Write something: ")
    set1.add(word)
    x += 1

y = 1
while y <= 4:
    word = input("Write something: ")
    set2.add(word)
    y += 1

def function(h,p):
    tot = h & p
    print(tot)

function(set1, set2)