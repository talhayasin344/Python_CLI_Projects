import random

while True:
    getInput=input("It's your turn. Enter 'rock', 'paper', or 'scissors': ").lower()
    getComputer=random.choice(['rock', 'paper', 'scissors'])
    
    if getInput not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
    elif getInput == getComputer:
        print(f"Computer chose {getComputer}. It's a tie!")
    elif (getInput == 'rock' and getComputer == 'scissors') or (getInput == 'paper' and getComputer == 'rock') or (getInput == 'scissors' and getComputer == 'paper'):
        print(f"Computer chose {getComputer}. You win!")
    else:
        print(f"Computer chose {getComputer}. You lose!")