#write a function that takes two tuples as input and returns a new tuple containing all the elements of the two tuples

tuple1 = ()
x = 1
print("First tuple")
while x <= 5:
    request = (input("Enter a number: "),)
    tuple1 += request
    x += 1

tuple2 = ()
y = 1
print("Second tuple")
while y <= 5:
    request = (input("Enter a number: "),)
    tuple2 += request
    y += 1

tuple3 = tuple1 + tuple2
print(tuple3)