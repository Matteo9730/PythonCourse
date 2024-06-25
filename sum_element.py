#Write a function that takes a list of numbers as input and returns the sum of all elements

list = []
x = 1
while x <= 5:
    request = int(input("Enter a number: "))
    list.append(request)
    x += 1

y = 0
for a in list:
    y += a
print(y)