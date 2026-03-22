cart = []

# Add a dictionary {"name": ..., "price": ..., "quanity":...} to cart
def add_item(name, price, qnt):
    cart.append({"name": name, "price": price, "quantity": qnt})


def show_cart():
    if len(cart) == 0:
        print("Your cart is empty 🛒")
    else:
        print("Your cart 🛒:")
        for item in cart:
            print(f" - {item['name']}   x{item['quantity']}    ₹{item['price']} per item")

#here we are using ne flag variable. What is flag variable?
# a flag variable is just a variable that tracks if something happened   
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


#Checkout function -> here this function evaluates the price of the each item and then add all item price to get toal price and then if total > 500 applies 10% discount, if total <= 500 then proceeds to check out.

def checkout():  #def checkout(item):   # ❌ why is item here? so correct is def checkout(): because checkout() doesn't need anything from outside. It already has access to cart directly - it doesn't need anything to pass from outside
    total = 0
    discount_per = 10/100
    for item in cart:
        total += item['price'] * item['quantity']
    if total <= 500:
        print(f"Total Price: {total}")
    else:
        discount = discount_per * total #discount applied
        total = total - discount
        print(f"Total price after discount of 10%: {total}")


# -------- MAIN MENU --------
while True:
    print("\n--- SHOPPING CART ---")
    print("\n 1. Add item")
    print("\n 2. Remove item")
    print("\n 3. Show cart")
    print("\n 4. Checkout")
    print("\n 5. Exit")

    choice = input("\n Choose:")

    if choice == "1":
        name =  input("\n Item name: ")
        price = float(input("\n Price: "))
        qnt = int(input("\n Quantity: "))
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

