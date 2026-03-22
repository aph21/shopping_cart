# 🛒 Shopping Cart — Python CLI Project

A command-line shopping cart application built in Python as part of a logic-building learning journey.
This project was built from scratch to practice core Python concepts like dictionaries, lists, functions, loops, and conditionals.

---

## 📌 Project Goal

The goal of this project was **not** to build a perfect application — but to **build logic**.
Every function was thought through, discussed, and coded step by step to develop problem-solving skills in Python.

---

## 🧠 Concepts Practiced

| Concept | Where Used |
|---|---|
| `list` | `cart = []` — stores all items |
| `dictionary` | Each item stored as `{"name", "price", "quantity"}` |
| List of Dictionaries | Entire cart structure |
| `for` loops | `show_cart()`, `remove_item()`, `checkout()` |
| `if / elif / else` | Discount logic, menu choices, empty cart check |
| Functions | Every feature is its own function |
| Flag Variable | `found` in `remove_item()` to track if item exists |
| f-strings | Displaying cart items cleanly |
| `while True` loop | Main menu that keeps running |
| `break` | Exits the menu when user chooses Exit |
| `.lower()` | Case-insensitive item removal |

---

## 🗂️ Project Structure

```
shopping_cart/
│
└── main.py       ← entire project lives here
```

---

## ⚙️ How It Works

### Data Structure

Each item in the cart is stored as a **dictionary** inside a **list**:

```python
cart = [
    {"name": "pen",   "price": 20.0, "quantity": 5},
    {"name": "apple", "price": 2.0,  "quantity": 15},
    {"name": "notes", "price": 50.0, "quantity": 2}
]
```

This approach was chosen because:
- A list allows multiple items
- A dictionary keeps name, price, and quantity together cleanly
- Easy to loop through and access each field by key

---

## 🚀 Features

### 1. Add Item
Takes `name`, `price`, and `quantity` from the user and appends a dictionary to the cart.

```python
def add_item(name, price, qnt):
    cart.append({"name": name, "price": price, "quantity": qnt})
```

### 2. Show Cart
Displays all items in the cart with a clean formatted output.
If cart is empty, shows a friendly message.

```python
def show_cart():
    if len(cart) == 0:
        print("Your cart is empty 🛒")
    else:
        print("Your cart 🛒:")
        for item in cart:
            print(f" - {item['name']}   x{item['quantity']}    ₹{item['price']} per item")
```

### 3. Remove Item
Searches for an item by name (case-insensitive) and removes it.
Uses a **flag variable** `found` to handle the "item not found" case safely.

```python
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
```

> 💡 **Why a flag variable?**
> After the loop ends, we can't rely on `item` to check if something was found —
> it only holds the last item looped over. A flag variable (`found`) reliably
> tracks whether a match was found at any point during the loop.

### 4. Checkout
Calculates the total price of all items (`price × quantity`).
Applies a **10% discount** if total exceeds ₹500.

```python
def checkout():
    total = 0
    discount_per = 10/100
    for item in cart:
        total += item['price'] * item['quantity']
    if total <= 500:
        print(f"Total Price: {total}")
    else:
        discount = discount_per * total
        total = total - discount
        print(f"Total price after discount of 10%: {total}")
```

### 5. Main Menu (while loop)
Keeps the program running until the user chooses to exit.
Handles invalid choices gracefully.

```
--- SHOPPING CART ---
 1. Add item
 2. Remove item
 3. Show cart
 4. Checkout
 5. Exit
```

---

## 🖥️ Sample Output

```
--- SHOPPING CART ---
 1. Add item
 ...
 Choose: 1
 Item name: pen
 Price: 20
 Quantity: 5

 Choose: 3
Your cart 🛒:
 - pen    x5    ₹20.0 per item
 - apple  x15   ₹2.0  per item

 Choose: 2
 Enter the item name to be removed: Apple
item removed

 Choose: 4
Total Price: 200.0

 Choose: 5
Bye! 👋
```

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

No external libraries needed — pure Python only.

---

## 🔑 Key Learnings

### input() always returns a string
```python
choice = input("Choose: ")   # returns "1", not 1
if choice == "1":            # must compare with string
```

### Dictionary keys must match exactly
```python
cart.append({"quantity": qnt})   # stored as "quantity"
item['quantity']                  # must access as "quantity"
item['qnt']                       # ❌ KeyError!
```

### Functions should do one job
Input collection happens outside the function.
The function only handles its own responsibility.
```python
# collect outside
name = input("Item name: ")
# pass inside
add_item(name, price, qnt)
```

---

## 🔲 Possible Upgrades

These were not implemented but are great next challenges:

- [ ] Prevent adding duplicate items
- [ ] Show total item count in `show_cart()`
- [ ] Sort cart by price before displaying
- [ ] Add quantity to existing item instead of duplicate
- [ ] Save cart to a file and load it back

---

## 👨‍💻 Built By

Built as a **logic-building exercise** while learning Python.
Every line was written, tested, debugged, and understood — not copied.

---