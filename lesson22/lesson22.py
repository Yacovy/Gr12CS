# Lesson 22
num = int(input())
num1 = 0
num2 = 1
shuffler = 0
for i in range(0,num):
    shuffler = num2
    num2 += num1
    num1 = shuffler
    
print(num1)