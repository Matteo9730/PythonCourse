#calculate the prime numbers between two numbers entered by the user

n1 = int(input("Enter a number: "))
n2 = int(input("Another one: "))

if n1 > n2:
    n1, n2 = n2, n1

for n in range(n1, n2+1):
    even = True
    for k in range(2, n):
        if n % k == 0:
            even = False
            break
    if even and n > 1:
        print(n)