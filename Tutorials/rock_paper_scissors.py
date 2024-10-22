import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])

users_choice = input('Do you want rock, paper, or scissors?')

if computer_choice == users_choice:
    print('tie')
elif users_choice == 'rock' and computer_choice == 'scissors':
    print('win')
elif users_choice == 'paper' and computer_choice == 'rock':
    print('win')
elif users_choice == 'scissors' and computer_choice == 'paper':
    print('win')
else: print('you lose, computer wins')  

# python rock_paper_scissors.py