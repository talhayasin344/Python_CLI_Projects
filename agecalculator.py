getAge=int(input("Enter your age."))

if getAge < 0:
    print("You are not born yet.")
elif getAge >= 13 and getAge < 17:
    print("You are a child.")
elif getAge >= 17 and getAge < 20:
    print("You are a teenager.")
elif getAge >= 20 and getAge < 65:
    print("You are an adult.")
elif getAge >= 65:
    print("You are a senior citizen.")
else:
    print("You are a minor.")