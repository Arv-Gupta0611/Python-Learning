def add_contact():
    name,contact,email,category=input().split()
    name=name.lower()
    if name in d:
        print("Do You want to overwrite the existing contact Yes/No")
        ch=input().lower()
        if (ch=='yes' or ch=='y'):
            d[name]=[contact,email,category]
    else:
        d[name]=[contact,email,category]
def view_all():
    if not d:
        print("No Contacts Found ")
    else:
        for name,details in d.items():
            print(f"Name: {name} \nContact: {details[0]} \nEmail: {details[1]} \nCategory:{details[2]} ")
def search_contact(name):
    if name not in d:
        srch=input("Please Enter Search: ")
        if srch in name:
            found = False

        for contact_name in d:
            if srch.lower() in contact_name.lower():
                print(f"Name: {contact_name}")
                print(f"Contact: {d[contact_name][0]}")
                print(f"Email: {d[contact_name][1]}")
                print(f"Category: {d[contact_name][2]}")
                found = True

        if not found:
            print("No Contact Found")
    else:
        print(f"Name: {name} \nContact: {d[name][0]} \nEmail: {d[name][1]} \nCategory:{d[name][2]} ") 
def update_contact(name):
    if name not in d:
        print("No Contact Found")
    else:
        print("Which field do you want to update?")
        print("1. Phone")
        print("2. Email")
        print("3. Category")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_phone = input("Enter new phone: ")
            d[name][0] = new_phone
            print("Phone updated successfully")

        elif choice == "2":
            new_email = input("Enter new email: ")
            d[name][1] = new_email
            print("Email updated successfully")

        elif choice == "3":
            new_category = input("Enter new category: ")
            d[name][2] = new_category
            print("Category updated successfully")

        else:
            print("Invalid choice")
def delete_contact(name):
    if name not in d:
        print("No Contact Found")
    else:
        confirm = input(f"Are you sure you want to delete {name}? (yes/no): ")

        if confirm.lower() == "yes":
            del d[name]
            print("Contact deleted successfully")

        else:
            print("Contact deletion cancelled")
d={}
while(True):
    print("======Contact Book=======")
    print("1. Add Contact ")
    print("2. View All ")
    print("3. Search ")
    print("4. Update ")
    print("5. Delete ")
    print("6. Exit ")
    print("=========================")
    choice=int(input())
    if choice==1:
        add_contact()
    elif choice==2:
        view_all()
    elif choice==3:
        names=input("Enter Name: ")
        search_contact(names)
    elif choice==4:
        nameup=input("Enter Name: ")
        update_contact(nameup)
    elif choice==5:
        namedel=input("Enter Name: ")
        delete_contact(namedel)
    elif choice==6:
        print("Thank you for using Contact Management System!")
        print("Have a great day!")
        print("Exiting Contact Management System. Goodbye!")
        break