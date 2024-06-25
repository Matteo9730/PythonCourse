"""
print the following figures on the screen
******
*****
****
***
**
*
#
##
###
####
#####
######

1 654321
12 54321
123 4321
1234 321
12345 21
123456 1
"""

for x in range(6, 0, -1):
    print(x * "*")

for y in range(1, 7):
    print(y * "#")

num = 6

for i in range(0, num):
    for j in range(0, 1 + i, 1):
        j += 1
        print(j, end="")
    print(" ", end="")
    for k in range(num + 1 - i, 1, -1):
        k -= 1
        print(k, end="")
    print('\n')
