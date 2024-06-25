#given the three sides of a triangle, determine whether the triangle is scalene, isosceles or equilateral

side1 = int(input("Enter the first side: "))
side2 = int(input("Now, the second side: "))
side3 = int(input("And the third one: "))

if (side1 == side2) and (side1 == side3):
    print("Equilateral triangle")
elif ((side1 != side2) and (side1 != side3)) and (side2 != side3):
    print("Scalene triangle")
else:
    print("Isosceles triangle")