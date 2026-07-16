import random

while True:
    getNum = int(input("Enter a number between 1 and 100: "))
    randomNum = round(random.randint(1, 100))
    
    if getNum < 1 or getNum > 100:
        print("Please enter a number between 1 and 100.")
    elif getNum == randomNum:
        print("Congratulations! You guessed the correct number.")
        break   
    elif getNum < randomNum:
        print("Your guess is too low. Go a bit higher.")
    else:
        print("Your guess is too high. Go a bit lower.")