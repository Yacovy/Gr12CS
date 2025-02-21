# Lesson 21
max = int(input())
count = 0
temp = 0
most = 0
for i in range(1,max+1):
    temp = 0
    for x in range(1,i+1):
        if i % x == 0:
            temp += 1
    if temp > count:
        most = i
        count = temp
print(most)


