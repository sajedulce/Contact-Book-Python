#This code is just a simple Python contact book using the dictionary. Here you can add contacts, view contacts, edit contacts, search contacts, and delete contacts.
#In edit contacts, you can change both contact name and phone number. 
contact = {}

def displaycontacts():
    print(contact.items())
    print("name \t \t phone")
    for key in contact:
        print("{} \t \t {}".format(key, contact.get(key)))

while True:
    choice =int(input("1. Add New Contact \n"
                                    "2. Search Contact \n"
                                    "3. Display Contacts \n"
                                    "4. Edit Contacts \n"
                                    "5. Delete Contact \n"
                                    "6. Exit \n"
                                    "Enter Any Number Between 1-6: "))
    if choice == 1:
        name = input("Enter Name of The Contact: ")
        phone = input("Enter Phone Number: ")
        contact[name] = phone
    elif choice == 2:
        searchcontact = input("Enter Contact Name: ")
        if searchcontact in contact:
            print(searchcontact,"Contact Number is: ", contact[searchcontact])
        else:
            print("Contact is not in Contact List")
    elif choice ==3:
        if not contact:
            print("Contact Book is empty")
        else:
            displaycontacts()
    elif choice == 4:
        editcontact = input("Enter Name to Edit Contact")
        if editcontact in contact:
            phone = input("Enter Number to Change: ")
            name = input("Enter Name to Change: ")
            contact[editcontact] = phone
            contact[editcontact] = name
            print("Contact Updated Succesfully")
            displaycontacts()
        else:
            print("Name is not found in Contact Book")
    elif choice == 5:
        del_contact = input("Enter Name to Delete Contact: ")
        if del_contact in contact:
            del_contact_confirm = input("Are you sure to delete the contact: (y/n)")
            if del_contact_confirm == "y" or "Y":
                contact.pop(del_contact)
                displaycontacts()
        else:
                print("Name is not found in Contact Book")
    else:
        break
