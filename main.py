cart = []

def add_item(name, price, qnt):
    cart.append({"name": name, "price": price, "quantity": qnt})

def show_cart():
    if len(cart) == 0:
        print("Your cart is empty 🛒")
    else:
        print("Your cart 🛒:")
        for item in cart:
            print(f" - {item['name']}   x{item['quantity']}    ₹{item['price']} per item")

#main menu 
name =  input("Item name: ")
price = float(input("Price: "))
qnt = int(input("Quantity: "))

add_item(name, price, qnt)
show_cart()
