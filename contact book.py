contact={}


def display_contact():
    print("name\t\tcontact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice = int(input("1. Add new contact \n 2. view contact \n 3. search contact \n 4. update contact \n 5. delete contact \n 6. Exit\n"))
    if choice == 1:
        name = input("Enter the contact name")
        phone =input("Enter the phone number")
        contact[name] = phone
    elif choice == 2:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice == 3:
        search_name = input("enter the contact name")
        if search_name in contact:
            print(search_name,"s contact number is",contact[search_name])
        else:
            print("name not found in contact book")
    elif choice == 4:
        edit_contact =input("enter the contact to be edited")
        if edit_contact in contact:
            phone = input("enter phoe number")
            contact[edit_contact] = phone
            print("contact updated")
            display_contact()
        else:
            print("name not found in contact book")
    elif choice == 5:
        del_contact = input("enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact yes/no")
            if confirm == 'yes':
                contact.pop(del_contact)
            display_contact()
        else:
            print("name is not found in contact book")
    else:
        break

        

