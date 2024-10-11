rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
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
---.__(___)
'''

#Write your code below this line 👇
import random

choices = {
    0: rock,
    1: paper,
    2: scissors
}

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.choice(list(choices.keys()))

print('User:\n')
print(choices[user_choice])

print('Computer:\n')
print(choices[computer_choice])

win_condition = {
    0: 2,
    1: 0,
    2: 1
}

if (win_condition[user_choice] == computer_choice):
    print('User Won!')
elif (user_choice == computer_choice):
    print('Draw!')
else:
    print('User Lost!')