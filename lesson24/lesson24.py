# Lesson 24

longest = 0 
longestN = ""
while 1==1:
    name = input("input a name or input x to exit program ")
    if name == "x":
        break
    if len(name) > longest:
        longest = len(name)
        longestN = name
print(longestN)