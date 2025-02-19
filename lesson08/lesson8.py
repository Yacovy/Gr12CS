# Lesson 8
wins = 0
for i in range(6):
    result = input(f"Input result for game {i+1} ")
    if result == "W":
        wins += 1
if wins > 4:
    print(1)
elif wins > 2:
    print(2)
elif wins > 0:
    print(3)
else:
    print(-1)