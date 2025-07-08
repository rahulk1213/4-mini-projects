contacts = []

while True:
    
    print(" enter your choice")
    print("1. create contact ")
    print("2. update contact ")
    print("3. view contact")
    print("5 exit")

    choice = int(input(" Enter your choice between (1-4)"))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact = {"name": name, "phone": phone}
        contacts.append(contact)
        print("✅ Contact created successfully!")


    elif choice == 2:
        old_name = input("Enter the contact name to update: ")
        if old_name in contacts:
            new_name = input("Enter the new name: ")
            index = contacts.index(old_name)
            contacts[index] = new_name
            print("✅ Contact updated!")
        else:
            print("❌ Contact not found!")

    elif choice == 3:
        if not contacts:
            print("No contact in the list.")
        else:
            print(" Your To-Do List:")
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact}")     

    else:
        if choice == 4:
         print("exiting the contack book ! good bye")
        else:
            print("invalid ! please enter between  (1-4)")
