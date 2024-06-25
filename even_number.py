#write a function that takes a list of numbers as input and returns a list containing only even numbers

list = []
x = 1
while x <= 5:
    request = int(input("Enter a number: "))
    list.append(request)
    x += 1

list1 = []
for y in list:
    if y % 2 == 0:
        list1.append(y)
    else:
        pass
print(list1)