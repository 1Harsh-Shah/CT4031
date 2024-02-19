import random

ans = random.randint(1, 100)
while True:
    player_ans = int(input("Enter a number between 1 and 10: "))
    if player_ans == ans:
        print("Congrats you got it!")
        break
    elif player_ans > ans:
        print("Lower!")
    elif player_ans < ans:
        print("Higher!")
    else:
        print("Please follow the instructions")

