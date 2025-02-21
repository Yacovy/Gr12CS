# Lesson 19
inp = int(input())
count = 0
for i in range(2,inp):
    if inp % i == 0:
        count += 1
        break
if count != 0:
    print("Not Prime")
else:
    print("Prime")