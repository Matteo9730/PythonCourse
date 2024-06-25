#write a function that takes a set and an element as input and returns True if the element is present in the set, otherwise False.
set1 = set()

x = 1
while x <= 4:
    word = input("Write something: ")
    set1.add(word)
    x += 1

a_word = input("Write something else: ")

def function(y,z):
    if z in y:
        print("True")
    else:
        print("False")

function(set1, a_word)