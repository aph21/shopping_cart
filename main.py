# Global list that stores all cart items as dictionaries
cart = []

# Adds an item to cart — each item is a dict so we can access name, price, quantity easily
def add_item(name, price, qnt):
    cart.append({"name": name, "price": price, "quantity": qnt})


# Displays all items in cart — loops through the list and prints each item's details
def show_cart():
    if len(cart) == 0:
        print("Your cart is empty 🛒")
    else:
        print("Your cart 🛒:")
        for item in cart:
            print(f" - {item['name']}   x{item['quantity']}    ₹{item['price']} per item")

# Removes an item by name — uses a flag variable (found) to track if the item existed
# .lower() on both sides makes the search case-insensitive ("Apple" matches "apple")
# break stops the loop early once we find and remove the item — no need to keep searching
def remove_item(name):
    found = False
    for item in cart:
        if item['name'].lower() == name.lower():
            cart.remove(item)
            print("item removed")
            found = True
            break
    if found == False:
        print("Item not found")


# Calculates total price — applies 10% discount if total > 500
# No parameters needed because cart is a global variable, accessible from anywhere
def checkout():
    total = 0
    discount_per = 10/100  # 10% stored as decimal for easy multiplication
    for item in cart:
        total += item['price'] * item['quantity']  # price of each item = unit price * quantity
    if total <= 500:
        print(f"Total Price: {total}")
    else:
        discount = discount_per * total
        total = total - discount
        print(f"Total price after discount of 10%: {total}")


# -------- MAIN MENU --------
# while True keeps the menu running forever until user picks "Exit" (break stops the loop)
while True:
    print("\n--- SHOPPING CART ---")
    print("\n 1. Add item")
    print("\n 2. Remove item")
    print("\n 3. Show cart")
    print("\n 4. Checkout")
    print("\n 5. Exit")

    choice = input("\n Choose:")  # input() always returns a string, so we compare with "1", "2" etc.

    if choice == "1":
        name =  input("\n Item name: ")
        price = float(input("\n Price: "))   # float() converts string to decimal number
        qnt = int(input("\n Quantity: "))    # int() converts string to whole number
        add_item(name, price, qnt)

    elif choice == "2":
        name = input("\n Enter the item name to be removed: ")
        remove_item(name)
    
    elif choice == "3":
        show_cart()

    elif choice == "4":
        checkout()

    elif choice == "5":
        print("Bye!👋")
        break
    else:
        print("Invalid Choice❌❌❌ (Choose between 1-5)")

