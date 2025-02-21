# Lesson 20
sum = 0
temp = 0
for i in range(1,10001):
    temp = 0
    for x in range (1,i):
        if i % x == 0:
            temp += x
    if temp == i:
        sum += i
print(sum)
        
