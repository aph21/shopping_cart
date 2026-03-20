cart = []

def add_item(name, price, qnt):
    cart.append({"name": name, "price": price, "quantity": qnt})

#main menu 
name =  input("Item name: ")
price = float(input("Price: "))
qnt = int(input("Quantity: "))

add_item(name, price, qnt)

#print(cart)