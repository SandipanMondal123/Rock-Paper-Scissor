import random

def start():

 
    computer = random.choice(['rock', 'paper', 'scissor'])
    user = input("Write 'rock' for ROCK, 'paper' for PAPER, 'scissor' for SCISSOR: ")

    if(computer == user):
        print("TIE. You both picked %s" % user)
    elif is_win(computer, user):
        print("You won!")
    else:
        print("You Lost :( ")
    
    again = input("Want to play again? 'n' for no and 'y' for yes: ")
    if again == 'n':
        return
    start();
        

def is_win(computer, user):
        return (computer == 'rock' and user == 'paper') or (computer == 'paper' and user == 'scissor') or (computer == 'scissor' and user == 'rock')

start()