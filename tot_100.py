"""
given two numbers, sum them up and check whether the result is greater than 100, displaying the
message 'the result is greater than 100' if yes and 'the result is not greater than 100' if not.

"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Now, the second one: "))
if num1 + num2 > 100:
    print("The result is greater than 100")
else:
    print("The result isn't greater than 100")