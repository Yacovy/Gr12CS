# Lesson 13
month = int(input())
day = int(input())

if month > 2:
    print("after")
elif month < 2:
    print("before")
else:
    if day > 18:
        print("after")
    elif day == 18:
        print('during')
    else: 
        print('before')

