"""
write a program that calculates a student's exam result.
the program will take in input:
- the grade obtained in the theory test (between -8 and +8)
- the grade obtained in the practice test (between 0 and 24)
Onche these data have been memorized, proceed to calculate the final result in thirtieths as follows:
- the final result is the sum of the results
- if the theory is less than or equal to 0 and the sum of the theory and practice is greater than 18, the student fails
- if the theory is less than or equal to 0 and the practice is less than 18, the student fails
- if the theory is greater than 0 and the sum of the theory and practice is less than 18, the student fails
- if the sum of theory and practice is 31 or 32, print 'congratulation: 30 with honours'
- in all other cases the student is promoted and the calculated grade is reported
"""

theory = -10
pratice = -1

while theory< -8 or theory > 8:
    try:
        theory = int(input("What grade did you get on the theory? "))
    except ValueError:
        print("It should be a number between -8 and +8")

while pratice < 0 or pratice > 24:
    try:
        pratice = int(input("In the practice? "))
    except ValueError:
        print("It should be a number between 0 and +24")


res = theory + pratice

if theory <= 0:
    print("The student fails")
elif theory >= 1 and pratice < 18:
    print("The student fails")
elif res > 30:
    print("Congratulation: 30 with honours")
else:
    print(f"The student passes. Here the result: {res}/30")