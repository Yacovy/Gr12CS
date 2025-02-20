# Lesson 10
phoneNum = input("Input the last 4 digits of the phone num ")

if not(phoneNum[0] == "8" or phoneNum[0] == "9"):
    print("answer")

elif not(phoneNum[3] == "8" or phoneNum[4] == "9"):
    print("answer")
elif not(phoneNum[2] == phoneNum[1]):
    print("answer")
else:
    print("ignore")


