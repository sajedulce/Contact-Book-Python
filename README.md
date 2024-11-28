# Contact Book Management System

This is a simple Python-based Contact Book Management system that allows users to manage their contacts. Users can perform various operations such as adding, searching, editing, deleting, and displaying contacts.

## Features

- **Add New Contact**: Add a contact by specifying a name and phone number.
- **Search Contact**: Search for a contact by name and display its corresponding phone number.
- **Display Contacts**: Display all contacts in the contact book.
- **Edit Contact**: Edit an existing contact's name or phone number.
- **Delete Contact**: Delete a contact from the contact book after confirming the deletion.
- **Exit**: Exit the application.

## Requirements

- Python 3.x

## How to Run

1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the script by executing the following command:

```bash
python contact_book.py
```

5. Follow the on-screen prompts to interact with the system.

## Usage

After running the script, the system will display a menu with the following options:

1. **Add New Contact**: Add a contact with a name and phone number.
2. **Search Contact**: Enter the name of a contact to view their phone number.
3. **Display Contacts**: View all contacts stored in the contact book.
4. **Edit Contact**: Modify the name or phone number of an existing contact.
5. **Delete Contact**: Delete a contact from the list after confirming the action.
6. **Exit**: Exit the program.

The system will continuously prompt the user for input until the user chooses to exit the program.

## Example

### Sample Interaction:

```bash
1. Add New Contact 
2. Search Contact 
3. Display Contacts 
4. Edit Contacts 
5. Delete Contact 
6. Exit 
Enter Any Number Between 1-6: 1
Enter Name of The Contact: John Doe
Enter Phone Number: 1234567890

1. Add New Contact 
2. Search Contact 
3. Display Contacts 
4. Edit Contacts 
5. Delete Contact 
6. Exit 
Enter Any Number Between 1-6: 3
name            phone
John Doe        1234567890

1. Add New Contact 
2. Search Contact 
3. Display Contacts 
4. Edit Contacts 
5. Delete Contact 
6. Exit 
Enter Any Number Between 1-6: 2
Enter Contact Name: John Doe
John Doe Contact Number is: 1234567890
```

## Contribution

Feel free to fork the repository and make pull requests for any improvements or bug fixes. Contributions are welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).
