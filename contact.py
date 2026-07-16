def printMenu():
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

contacts=[]
found=False

def confirmAgain():
    while True:
        reconfirmation=input("Do you want to start again? yes/no? ")
        if reconfirmation == "yes":
            return True
        elif reconfirmation == "no":
            return False

while True:
    printMenu()
    getinput=int(input("Select an option from the menu with a number. "))
    if getinput == 1:
        getName=input("Enter the name of the contact. ")
        getPhone=input("Enter the phone number of the contact. ")
        getEmail=input("Enter the email of the contact. ")
        contacts.append({
            "name": getName,
            "phone": getPhone,
            "email": getEmail
        })
        print("Your contact has been saved. ")
        if not confirmAgain():
            break
    elif getinput == 2:
        print("---------- View Contacts ----------")
        for i in range(len(contacts)):
            print(f"{i}. Contact name: {contacts[i]["name"]}")
            print(f"{i}. Contact phone: {contacts[i]["phone"]}")
            print(f"{i}. Contact email: {contacts[i]["email"]}")
        if len(contacts) == 0:
            print("No contact found. ")
        if not confirmAgain():
            break
    elif getinput == 3:
        search=input("Search by name, phone, or email. ")
        for i in range(len(contacts)):
            if search == contacts[i]["name"] or search == contacts[i]["phone"] or search == contacts[i]["email"]:
                print(f"The contact you're trying to find is {contacts[i]["name"]}, {contacts[i]["phone"]}, {contacts[i]["email"]}")
                found=True
                update=input("Do you want to update this contact? yes/no? ")
                if update == "yes":
                    updatedName=input("Enter the name you want to update to. ")
                    updatedPhone=input("Enter the phone number you want to update to. ")
                    updatedEmail=input("Enter the email you want to update to. ")
                    contacts[i]["name"]=updatedName
                    contacts[i]["phone"]=updatedPhone
                    contacts[i]["email"]=updatedEmail
                    print("Your contact has been successfully updated. ")
                    break
        if not confirmAgain():
            break
    elif getinput == 4:
        del_contact=int(input("Enter the number of the contact you want to delete. "))
        if del_contact > len(contacts) or del_contact < 0:
            print("Your entered number is not available. Please enter the right number. ")
            break
        else:
            contacts.pop(del_contact)
            print("Your contact has successfully deleted. ")
        if not confirmAgain():
            break
    elif getinput == 5:
        break
    else: 
        print("Invalid input ")
        break
