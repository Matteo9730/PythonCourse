#write a function that takes a tuple and an index as input and returns the element corresponding to the index

tuple1 = ()
x = 1
while x <= 5:
    request = (input("Enter something: "),)
    tuple1 += request
    x += 1
index = int(input("Write a number: "))
print(tuple1[index])