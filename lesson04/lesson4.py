# Lesson 4
len1 = len(input())
len2 = len(input())
len3 = len(input())
print(len1+len2+len3)
print((len1+len2+len3)%12)

if (len1+len2+len3) % 12 == 0:
    print(((len1+len2+len3)/12)* 14.95)
else:
    print((((len1+len2+len3)//12)+1)* 14.95)