# Lesson 9

import random
invalid = True
valid = ["scissors","rock","paper"]
while invalid:
    pick = input("Input rock, paper or scissors ")
    if pick in valid:
        invalid = False
AI = random.choice(valid)
if AI == pick:
    print("The result is a tie")
elif pick == "scissors":
    if AI == "rock":
        print("The result is a win for the AI")
    if AI == "paper":
        print("The result was a win for the Player")
elif pick == "rock":
    if AI == "paper":
        print("The result is a win for the AI")
    if AI == "scissors":
        print("The result was a win for the Player")
elif pick == "paper":
    if AI == "rock":
        print("The result was a win for the Player")
    if AI == "scissors":
         print("The result is a win for the AI")
    

    