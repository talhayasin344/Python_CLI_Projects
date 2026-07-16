from datetime import datetime
import random

characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
store_otp=""

def printMenu():
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

def generate_otp():
    store_otp=""
    for i in range(5):
        gen_otp=random.choice(characters)
        store_otp += gen_otp

    return store_otp

pin=1234
balance=1000
transection_history=[
    {
        "amount": 0,
        "dateandtime": 0,
        "disc": ""
    }
]

while True:
    getpin=int(input("Type your 4 digit PIN to access your account. "))
    if getpin != pin:
        print("Enter a valid PIN. ")
        break
    
    printMenu()
    getselection=int(input("Type the number here from the list above. "))

    if getselection == 1:
        print(f"Your current balance is ${balance}") 
        continue
    elif getselection == 2:
        deposit=int(input("Enter the amount of money you need to deposit. "))
        store_otp=generate_otp()
        print("The OTP you received is", store_otp)
        getotp=input("Enter the OTP you received. ")

        if getotp == store_otp:
            print("Correct, OTP ")
            store_otp=""
            if deposit <= 0:
                print("Enter a valid amount. ")
            else:
                balance += deposit
                print(f"The amount of {deposit} Is added to your account ")
                transaction_time=datetime.now()
                transection_history.append({
                    "amount": deposit,
                    "dateandtime": transaction_time,
                    "disc": "The deposit amount is successfully credited to your account. "
                })
            continue
        else:
            print("Enter the right OTP. ")
            break
        
    elif getselection == 3:
        withdraw=int(input("Enter the amount you want to withdraw. ")) 
        store_otp=generate_otp()
        print("The OTP you received is", store_otp)
        getotp=input("Enter the OTP you received. ")

        if getotp == store_otp:
            print("Correct, OTP ")
            store_otp=""
            if withdraw <= 0:
                print("Please enter a valid withdrawal amount. ")
            elif withdraw > balance:
                print("Not enough balance. ")
            else: 
                balance -= withdraw
                print(f"The amount of {withdraw} Is Deducted from your account ")
                transaction_time=datetime.now()
                transection_history.append({
                    "amount": withdraw,
                    "dateandtime": transaction_time,
                    "disc": "The withdrawal amount is successfully deducted from your account. "
                })
            continue
        else:
            print("Enter the right OTP. ")
            break
    elif getselection == 4:
        print('--------- Transactional History ---------')
        for i in range(1,len(transection_history)):
            print(transection_history[i]["disc"])
            print(f"Amount is. ${transection_history[i]["amount"]}")
            print(transection_history[i]["dateandtime"])
        continue
    elif getselection == 5:
        break
    else:
        print("Enter your valid value. ")
        continue