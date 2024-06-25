"""
write a program that uses a for loop to calculate the sum of the first n even numbers, where n is a number entered
by the user
"""

n = int(input("Enter a number: "))
prime = 1
tot = 0

while prime < n:
    if prime % 2 == 0:
        tot += prime
    else:
        pass
    prime += 1
print(tot)
