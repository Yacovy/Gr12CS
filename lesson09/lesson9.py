# Lesson 9

import random
pick = ""
while pick !="stop":
    invalid = True
    valid = ["scissors","rock","paper","stop"]

    while invalid:
        pick = input("Input rock, paper or scissors or stop to stop ")
        if pick in valid:
            invalid = False
    if pick !="stop":
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


