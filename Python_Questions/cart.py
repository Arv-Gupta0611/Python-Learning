catalogue = {
    "P001": {"name": "Notebook", "price": 45, "category": "Stationery"},
    "P002": {"name": "Pen", "price": 10, "category": "Stationery"},
    "P003": {"name": "Pencil", "price": 5, "category": "Stationery"},
    "P004": {"name": "School Bag", "price": 600, "category": "Accessories"},
    "P005": {"name": "Headphones", "price": 800, "category": "Electronics"},
    "P006": {"name": "Mouse", "price": 350, "category": "Electronics"},
    "P007": {"name": "Water Bottle", "price": 150, "category": "Accessories"},
    "P008": {"name": "Keyboard", "price": 500, "category": "Electronics"}
}
cart={}
while True:
    print("1. View Catalogue")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("--------Catalogue----------")
        for prod_id , details in catalogue.items():
            print(f"{prod_id}  {details['category']}  {details['name']}  ₹{details['price']}")

    
    elif choice == "2":
        prod_id=input("Enter Product Id ").upper()
        quantity = int(input("Enter the quantity: "))
        if prod_id in catalogue:
            if prod_id in cart:
                cart[prod_id] += quantity
            else:
                cart[prod_id]=quantity
            print("Item added Sucessfully")
        else:
            print("Product not found ")

    elif choice == "3":
        prod_id=input("Enter Product Id ").upper()
        if prod_id in cart:
            del cart[prod_id]
            print("Item removed sucessfully")
        else:
            print("Product not found ")

    elif choice == "4":
        print("-----------Cart------------")
        for item,qty in cart.items():
            print(f"{item}      {qty}")

    elif choice == "5":
        subtotal=0
        print("----------Bill-----------")
        for prod, qty in cart.items():
            product=catalogue[prod]
            name=product['name']
            price=product['price']
            line_total = price * qty

            print(f"{name:<15} x{qty}  ₹{line_total:.2f}")
            subtotal += line_total

            discount = 0

            if subtotal > 500:
                discount = subtotal * 0.10

            final_amount = subtotal - discount

            print("-------------------------")
            print(f"Subtotal:       ₹{subtotal:.2f}")
            print(f"Discount:       ₹{discount:.2f}")
            print("-------------------------")
            print(f"Total:          ₹{final_amount:.2f}")
            print("=========================")

        cart.clear()
        print("Checkout complete! Cart cleared.")


    elif choice == "6":
        print("Thank you for shopping!")
        break


    else:
        print("Invalid choice")