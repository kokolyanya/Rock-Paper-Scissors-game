import random

def play():
    print("WELCOME !!!\n*****This is a ROCK-PAPER-SCISSORS game with the computer,\nRock is stronger than scissors,\n\
Scissors is stronger than paper,\nAnd paper is stronger than rock.*****\n")
    user=''
    while(user != 'r' and user != 'p' and user != 's') :
        user = input("What's your choice ? 'r' for rock, 'p' for paper or 's' for scissors\n")
    
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie !!!'

    if isWin(user,computer):
        return 'You win !!!'

    return f'You lost !!! The computer choose {computer}'

def isWin(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else :
        return False

print(play())