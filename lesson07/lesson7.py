# Lesson
import random
DC = int(input("Please input the required DC "))
D20 = random.randrange(0,21)
print(D20)
if D20 >= DC:
    print("You passed the DC")
else:
    print("you failed the DC")