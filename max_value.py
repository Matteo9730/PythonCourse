#calculates the maximum value between three numbers

list = [2,4,6]
max = list[0]

for i in list:
    if i > max:
        max= i
print(max)