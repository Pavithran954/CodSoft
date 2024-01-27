import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import *

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x550")

        self.contacts = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack(pady=10)

        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack(pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack(pady=10)

        self.email_entry = tk.Entry(root)
        self.email_entry.pack(pady=5)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack(pady=10)

        self.address_entry = tk.Entry(root)
        self.address_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=10)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{i + 1}. {contact['Name']} - {contact['Phone']}" for i, contact in enumerate(self.contacts)])
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts available.")

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']]
            if results:
                result_list = "\n".join([f"{contact['Name']} - {contact['Phone']}" for contact in results])
                messagebox.showinfo("Search Results", result_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def update_contact(self):
        if not self.contacts:
            messagebox.showerror("Error", "No contacts available.")
            return

        selected_contact = simpledialog.askstring("Update Contact", "Enter the name of the contact you want to update:")
        if selected_contact:
            for contact in self.contacts:
                if contact["Name"].lower() == selected_contact.lower():
                    new_phone = simpledialog.askstring("Update Contact", "Enter the new phone number:")
                    new_email = simpledialog.askstring("Update Contact", "Enter the new email:")
                    new_address = simpledialog.askstring("Update Contact", "Enter the new address:")
                    contact["Phone"] = new_phone if new_phone else contact["Phone"]
                    contact["Email"] = new_email if new_email else contact["Email"]
                    contact["Address"] = new_address if new_address else contact["Address"]
                    messagebox.showinfo("Success", "Contact updated successfully!")
                    return
            messagebox.showerror("Error", f"Contact with name {selected_contact} not found.")
        else:
            messagebox.showerror("Error", "Please enter a contact name.")

    def delete_contact(self):
        if not self.contacts:
            messagebox.showerror("Error", "No contacts available.")
            return

        selected_contact = simpledialog.askstring("Delete Contact", "Enter the name of the contact you want to delete:")
        if selected_contact:
            for contact in self.contacts:
                if contact["Name"].lower() == selected_contact.lower():
                    self.contacts.remove(contact)
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                    return
            messagebox.showerror("Error", f"Contact with name {selected_contact} not found.")
        else:
            messagebox.showerror("Error", "Please enter a contact name.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)

    #icon
    Image_icon=PhotoImage(file="ContactBook.png")
    root.iconphoto(False,Image_icon)
    
    root.mainloop()