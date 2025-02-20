# Lesson 11
inp = input()
inp = inp.split(' ')
inp = list(map(int,inp))
x,y = inp
if x > 0:
    if y > 0: 
        print('the point is in quadrant 1')
    else:
        print("the point is in quadrant 4")
elif y>0:
    print("the point is in quadrant 2 ")
else:
    print('the points is in quadrant 3')