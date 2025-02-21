# Lesson 25
num = int(input())
SubFactor = 0
largest = 0
for i in range(1,num):
    SubFactor = 0
    if num % i == 0:
        for x in range(1,i):
            if i % x == 0:
                SubFactor += 1
        if SubFactor == 1:
            largest = i
print(largest)


