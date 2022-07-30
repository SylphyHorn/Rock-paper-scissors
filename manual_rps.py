import random

def get_computer_choice():
    list  = ['Rock', 'Paper', 'Scissors']
    return random.choice(list)

def get_user_choice():
    choice= input('Please input(Rock, Paper, Scissors):')
    return choice

def get_winner(computer_choice, user_choice):
    computer_win = (computer_choice == 'Rock' and user_choice == 'Scissor') or (computer_choice == 'Scissors' and user_choice == 'Paper') or (computer_choice == 'Paper' and user_choice == 'Rock')
    if computer_win:
        return 'computer'
    elif computer_choice == user_choice:
        return 'draw'
    else:
        return 'user'

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(get_winner(computer_choice, user_choice))

play()