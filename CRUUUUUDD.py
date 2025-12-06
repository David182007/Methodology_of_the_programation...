# Name: Axel David Ortiz Reyna
# Matriculation: 2530152
# Group: IM 1-3

# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# A CRUD system (Create, Read, Update, Delete) lets users manage
# data through basic operations typically used in databases and
# inventory systems. This program uses a dictionary-of-dictionaries
# to store items, because it allows fast access by id and simple
# update logic. Using functions improves modularity and code
# organization. The program implements a menu-based interface that
# performs creation, reading, updating, deleting and listing of items.
#
# ------------------------------------------------------------
# PROBLEM: In-memory CRUD manager with functions
#
# Description:
# Program that implements a simple CRUD to manage items stored
# in a dictionary using independent functions for each operation.
#
# Inputs:
# - Menu option (0..5)
# - CREATE/UPDATE: item_id, name, price, quantity
# - READ/DELETE: item_id
#
# Outputs:
# - "Item created", "Item updated", "Item deleted",
#   "Item not found", "Items list:", etc.
#
# Validations:
# - Menu option must be valid.
# - item_id must not be empty.
# - price must be float >= 0.0
# - quantity must be int >= 0
# - No duplicates allowed when creating.
# - Must exist when reading/updating/deleting.
#
# Test cases:
# 1) Normal case:
#    create item → read it → update → delete → expected success messages.
# 2) Border case:
#    create item with quantity = 0 → expected valid creation.
# 3) Error case:
#    invalid option or non-numeric price → "Error: invalid input".
#
# Diagram (text description):
# Start → Show menu → Read option → Validate →
#   If create/read/update/delete/list →
#       call corresponding function →
#       print result →
#   If exit → stop program.
#
# Data structure decision:
# OPTION A chosen: dict where key=item_id and value=another dict.
# Reason: fast O(1) lookups, simple CRUD logic, clean code.
#
# ------------------------------------------------------------


# ------------------------------
# PROGRAM STARTS HERE
# ------------------------------

# Data storage
items_data = {}  # { item_id: {"name":..., "price":..., "quantity":...} }

# Constants
EXIT_OPTION = "0"


# ------------------------------
# CRUD FUNCTIONS
# ------------------------------

def create_item(data, item_id, name, price, quantity):
    """Create a new item if the id does not already exist."""
    if item_id in data:
        return False  # Duplicate
    data[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(data, item_id):
    """Return an item dict or None."""
    return data.get(item_id)


def update_item(data, item_id, name, price, quantity):
    """Update an existing item. Return True if updated."""
    if item_id not in data:
        return False
    data[item_id]["name"] = name
    data[item_id]["price"] = price
    data[item_id]["quantity"] = quantity
    return True


def delete_item(data, item_id):
    """Delete an item by id. Return True if successful."""
    if item_id in data:
        del data[item_id]
        return True
    return False


def list_items(data):
    """Print the list of all items."""
    print("Items list:")
    if not data:
        print("  (empty)")
        return
    for item_id, info in data.items():
        print(f"  ID: {item_id} | Name: {info['name']} | Price: {info['price']} | Qty: {info['quantity']}")


# ------------------------------
# INPUT VALIDATION HELPERS
# ------------------------------

def validate_id(item_id):
    return item_id.strip() != ""


def validate_price(price_str):
    try:
        price = float(price_str)
        return price if price >= 0 else None
    except ValueError:
        return None


def validate_quantity(qty_str):
    try:
        qty = int(qty_str)
        return qty if qty >= 0 else None
    except ValueError:
        return None


# ------------------------------
# MAIN PROGRAM LOOP
# ------------------------------

def main():
    while True:
        print("\n--- MENU ---")
        print("1) Create item")
        print("2) Read item by id")
        print("3) Update item by id")
        print("4) Delete item by id")
        print("5) List all items")
        print("0) Exit")

        option = input("Select an option: ")

        if option == EXIT_OPTION:
            print("Exiting program...")
            break

        # CREATE
        if option == "1":
            item_id = input("Item id: ")
            if not validate_id(item_id):
                print("Error: invalid input")
                continue

            name = input("Item name: ").strip()
            price = validate_price(input("Price: "))
            quantity = validate_quantity(input("Quantity: "))

            if price is None or quantity is None:
                print("Error: invalid input")
                continue

            if create_item(items_data, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: invalid input (duplicate id)")

        # READ
        elif option == "2":
            item_id = input("Item id: ")
            item = read_item(items_data, item_id)
            if item is None:
                print("Item not found")
            else:
                print(f"Item found: Name={item['name']}, Price={item['price']}, Quantity={item['quantity']}")

        # UPDATE
        elif option == "3":
            item_id = input("Item id: ")
            if item_id not in items_data:
                print("Item not found")
                continue

            name = input("New name: ").strip()
            price = validate_price(input("New price: "))
            quantity = validate_quantity(input("New quantity: "))

            if price is None or quantity is None:
                print("Error: invalid input")
                continue

            if update_item(items_data, item_id, name, price, quantity):
                print("Item updated")
            else:
                print("Item not found")

        # DELETE
        elif option == "4":
            item_id = input("Item id: ")
            if delete_item(items_data, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        # LIST
        elif option == "5":
            list_items(items_data)

        else:
            print("Error: invalid input")


# Run program
if __name__ == "__main__":
    main()


# ------------------------------------------------------------
# CONCLUSIONS
# Using functions greatly simplified the organization of the
# CRUD logic, making the program more readable and modular.
# A dictionary structure allowed constant-time lookups and
# simplified update/delete operations. Input validation was
# challenging but essential to ensure correct behavior across
# all operations. This CRUD could be expanded by adding file
# persistence, databases, authentication, or pagination.
#
# ------------------------------------------------------------
# REFERENCES
# 1. “Python Dictionaries”, Python.org Documentation
# 2. “Clean Code”, Robert C. Martin
# 3. “Designing Data-Intensive Applications”, Martin Kleppmann
# ------------------------------------------------------------
