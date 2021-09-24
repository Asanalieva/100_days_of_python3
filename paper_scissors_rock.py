import random

player = int(input("0 rock, 1 paper, 2 scissors: "))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.(___)
'''

# My choice printed
if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print(scissors)
else:
    print("Please try again.")

# Computer's random choice
computer = random.randint(0, 2)
print("computer chose:")

# Computer  choice printed
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)
else:
    print("Please try again.")

# Winner's code
if player == computer:
    print("Draw!")
elif player == 0 and computer == 2:
    print("You win!")
elif player < computer:
    print("Computer win!")
elif player > computer:
    print("You win!")
elif player == 2 and computer == 0:
    print("Computer win!")