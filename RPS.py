import random

list = [1,2,3]
computer_random = random.choice(list)
print(computer_random)

user_input = input("Choose rock, paper or scissors")
user_answer = 0
if user_input == "rock":
    user_answer = 1
elif user_input == "paper":
    user_answer = 2
elif user_input == "scissors":
    user_answer = 3
else:
    print("You need to choose between rock, paper or scissors")
print(user_answer)
if user_answer == computer_random:
    print("tie")
elif user_answer == 1 and computer_random == 2:
    print("computer wins")
elif user_answer == 1 and computer_random == 3:
    print("you win")
elif user_answer == 2 and computer_random == 1:
    print("you win")
elif user_answer == 2 and computer_random == 3:
    print("computer wins")
elif user_answer == 3 and computer_random == 1:
    print("computer wins")
elif user_answer == 3 and computer_random == 2:
    print("you win")