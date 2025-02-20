# Lesson 12
ang1 = int(input())
ang2 = int(input())
ang3 = int(input())
total = ang1 + ang2 + ang3
if total == 180:
    if ang1 == ang2 == ang3:
        print("Equilateral")
    elif ang1 == ang2 or ang2 == ang3 or ang1 == ang3:
        print("Isoceles")
    else:
        print("Scalene")
else:
    print("error")