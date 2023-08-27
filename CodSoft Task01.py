
#Internship @CodSoft - Task (1)
"""Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction.
"""

class contact_details:
    
    def __init__(self,name,phone_number,email_id,address):
        
        """
        Represents a contact with its name, phone_number , email_id and address.

        Args:
            name (str): The name of the Contact.
            phone_number (int): The phone number of the Contact.
            email_id (str): The email address of the Contact.
            address (str): The address of the Contact.
        """
        
        self.name=name
        self.phone_number=phone_number
        self.email_id = email_id
        self.address = address
        self.next = None
        
class ContactBook:
    
    """
    
    Contact Book class handles the addition, displaying, searching, updation and deletion of contacts.
    
    """
    
    def __init__(self):
        
        self.head=None
    
    def addContact(self,contact):
        
        """
        Adds a contact to the contact book.
        
        Args:
            contact (object): The object/instance of contact_details class.
        """
        
        if self.head is None:
            self.head=contact
        else:
            curNode = self.head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next=contact
    
    def displayContact(self):
         
        """
        
        Displays all the contacts in the contact book.
        
        """
        curNode = self.head
        while curNode is not None:
            print("Contact Details: ")
            print("Name : " , curNode.name)
            print("Phone Number : ", curNode.phone_number)
            print("Email Address : " , curNode.email_id)
            print("Address : ",  curNode.address)
            print()
            curNode = curNode.next
            
    def updateContact(self,name,phone,mail,addr):
        
        """
        Updates a contact in the contact book.

        Args:
            name (str): The name of the contact.
            phone (int) : The updated number of the contact.
            mail (str): The updated mail of the contact.
            addr (str): The updated address of the contact.
        """
        curNode = self.head
        while curNode:
            if curNode.name==name:
                curNode.phone_number=phone
                curNode.email_id=mail
                curNode.address=addr
                print("Contact Updation Succesful!")
                return
            curNode=curNode.next
        print("Contact Not Found")
                
    def searchContact(self,name):
        
        """
        Searches for a contact in the contact book.

        Args:
            name (str): The name of the contact.
        """
        
        curNode=self.head
        while curNode:
            if curNode.name==name:
                print("Contact Details: ")
                print("Name : " , curNode.name)
                print("Phone Number : ", curNode.phone_number)
                print("Email Address : " , curNode.email_id)
                print("Address : ",  curNode.address)
                print()
                return
            curNode = curNode.next
        print("Contact Not Found")
    
    def deleteContact(self,name):
        
                
        """
        Deletes a contact from the contact book.
        
        Args:
            name (str): The name of the contact to be deleted.
        """
        
        if self.head and self.head.name == name:
            self.head = self.head.next
            print("Contact deleted successfully.")
            return
        
        curNode = self.head
        prev = None
        while curNode:
            if curNode.name == name:
                prev.next = curNode.next
                print("Contact deleted successfully.")
                return
            prev = curNode
            curNode = curNode.next
        print("Contact not found.")

contact_book = ContactBook()

while True:
        print()
        print("Contact Book Menu:")
        print("1. Add a Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print()
        
        choice = int(input("Enter your choice: (1-6)  "))
        
        if choice==1:
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = contact_details(name, phone_number, email, address)
            contact_book.addContact(new_contact)
            print("Contact added!")
            
        elif choice==2:
            contact_book.displayContact()
            
        elif choice==3:
            name = input("Enter name: ")
            contact_book.searchContact(name)
            
        elif choice==4:
            name = input("Enter contact name: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.updateContact(name, new_phone_number, new_email, new_address)
        
        elif choice==5:
            name = input("Enter contact name: ")
            contact_book.deleteContact(name)
            
        elif choice==6:
            print("Exiting the Contact Book")
            break
        
        else:
            print("Invalid Choice......Try Again")






