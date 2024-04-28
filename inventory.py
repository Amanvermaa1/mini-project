inventory = {
        "A1": {"name": "Guava", "price": 16, "quantity": 100},
        "B2": {"name": "Pineapple", "price": 28, "quantity": 40},
        "C3": {"name": "Badam shake", "price": 50, "quantity": 80},
    }

cart = {}
total_amount = 0

print("Welcome to the Supermarket!")

while True:
        print("\nAvailable Items:")

        for id, details in inventory.items():
            print(f"{id}: {details['name']} - ₹{details['price']} ({details['quantity']} in stock)")

        print("\n1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in ['1', '3']:

            id = input("Enter the ID of the item: ")

            if id in inventory:

                if choice == '1':
                    qty_avail = inventory[id]["quantity"]
                    qty = int(input(f"Enter quantity (available: {qty_avail}): "))

                    if qty <= qty_avail:
                        inventory[id]["quantity"] -= qty
                        cart[id] = cart.get(id, 0) + qty
                        total_amount += qty * inventory[id]["price"]
                        print(f"{qty} {inventory[id]['name']} added to cart!")

                    else:
                        print(f"Insufficient quantity of {inventory[id]['name']} available.")

                else:

                    if id in cart:
                        qty_cart = cart[id]
                        qty = int(input(f"Enter quantity to remove (in your cart: {qty_cart}): "))

                        if qty <= qty_cart:
                            inventory[id]["quantity"] += qty
                            cart[id] -= qty
                            total_amount -= qty * inventory[id]["price"]
                            if cart[id] == 0:
                                del cart[id]
                            print(f"{qty} {inventory[id]['name']} removed from cart.")

                        else:
                            print(f"Insufficient quantity of {inventory[id]['name']} in your cart.")

                    else:
                        print(f"Item with ID '{id}' not found in your cart.")

        elif choice == '2':

            if not cart:
                print("Your cart is empty.")

            else:
                print("\nYour Cart:")
                for id, qty in cart.items():
                    details = inventory[id]
                    print(f"{qty} {details['name']} - ₹{details['price']} each")
                print(f"\nTotal Amount: ₹{total_amount}")

        elif choice == '4':

            if not cart:
                print("Your cart is empty. Please add items before checkout.")

            else:
                print("\nYour Cart:")
                for id, qty in cart.items():
                    details = inventory[id]
                    print(f"{qty} {details['name']} - ₹{details['price']} each")
                print(f"\nTotal Amount: ₹{total_amount}")
                print("\nYou only have to use cash any other method is not allowed")
                print("\nThank you for shopping!")
                break

        elif choice == '5':
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice. Please try again.")