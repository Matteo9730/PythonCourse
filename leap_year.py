#checks whether a uear is a leap year

year = int(input("Enter one year: "))
if ((year % 4 == 0) or (year % 100 == 0)) or (year % 400 == 0):
    print("Leap year")
else:
    print("Normal year")