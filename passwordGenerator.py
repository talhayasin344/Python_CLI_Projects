import random

while True:
    passwordLen=int(input("What should be the length of your password?"))
    
    store_pass=""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    for i in range(passwordLen):
        password=random.choice(characters)
        store_pass+=password
    
    print(store_pass)