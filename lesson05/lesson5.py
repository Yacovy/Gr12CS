# Lesson 5
money = input("How much money did you start with ")
cookies = input("What cookies did you sell ")
bcookie = cookies.count("b")
ncookie = cookies.count("c")
print(f"you sold {len(cookies)} cookies")
print(f"you made: {bcookie * 1.25 + ncookie * 0.75} dollars")
print(f"Your total money now is: {int(money) + bcookie * 1.25 + ncookie * 0.75}")