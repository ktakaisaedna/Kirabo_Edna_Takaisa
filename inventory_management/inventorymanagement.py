def main():
    inventory = {
        "sticky notes": {"price": 2000, "quantity": 15},
        "highlighter": {"price": 3500, "quantity": 25},
        "notebook": {"price": 10000, "quantity": 10},
    }
    
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. View all items")
        print("2. Add new item")
        print("3. Update item quantity")
        print("4. Update item price")
        print("5. Remove item")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            view_all_items(inventory)
        elif choice == "2":
            add_new_item(inventory)
        elif choice == "3":
            update_quantity(inventory)
        elif choice == "4":
            update_price(inventory)
        elif choice == "5":
            remove_item(inventory)
        elif choice == "6":
            print("Thank you for using the Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

def view_all_items(inventory):
    """Display all items in the inventory using a loop"""
    print("\n===== CURRENT INVENTORY =====")
    print("Item Name\tPrice (shs)\tQuantity")
    print("-" * 40)
    
    if not inventory:
        print("Inventory is empty!")
        return
    
    for item_name, item_data in inventory.items():
        print(f"{item_name}\t\tshs{item_data['price']:.2f}\t\t{item_data['quantity']}")

def add_new_item(inventory):
    """Add a new item to the inventory"""
    item_name = input("\nEnter item name: ").lower()
    
    if item_name in inventory:
        print(f"'{item_name}' already exists in inventory!")
        return

    try:
        price = float(input("Enter item price: $"))
        quantity = int(input("Enter item quantity: "))
        
        if price < 0 or quantity < 0:
            print("Price and quantity must be positive values!")
            return
        
        inventory[item_name] = {"price": price, "quantity": quantity}
        print(f"'{item_name}' added to inventory successfully!")
    except ValueError:
        print("Invalid input. Price must be a number and quantity must be an integer.")

def update_quantity(inventory):
    """Update the quantity of an existing item"""
    view_all_items(inventory)
    
    item_name = input("\nEnter item name to update quantity: ").lower()
    
    if item_name not in inventory:
        print(f"'{item_name}' not found in inventory!")
        return
    
    try:
        current_quantity = inventory[item_name]["quantity"]
        print(f"Current quantity of '{item_name}': {current_quantity}")
        
        new_quantity = int(input("Enter new quantity: "))
        
        if new_quantity < 0:
            print("Quantity must be a positive value!")
            return
        
        inventory[item_name]["quantity"] = new_quantity
        print(f"Quantity of '{item_name}' updated to {new_quantity}!")
    except ValueError:
        print("Invalid input. Quantity must be an integer.")

def update_price(inventory):
    """Update the price of an existing item"""
    view_all_items(inventory)
    
    item_name = input("\nEnter item name to update price: ").lower()
    
    if item_name not in inventory:
        print(f"'{item_name}' not found in inventory!")
        return
    
    try:
        current_price = inventory[item_name]["price"]
        print(f"Current price of '{item_name}': shs{current_price:.2f}")
        
        new_price = float(input("Enter new price: shs"))
        
    
        if new_price < 0:
            print("Price must be a positive value!")
            return
        
        inventory[item_name]["price"] = new_price
        print(f"Price of '{item_name}' updated to shs{new_price:.2f}!")
    except ValueError:
        print("Invalid input. Price must be a number.")

def remove_item(inventory):
    """Remove an item from the inventory"""
    view_all_items(inventory)
    
    item_name = input("\nEnter item name to remove: ").lower()
    

    if item_name not in inventory:
        print(f"'{item_name}' not found in inventory!")
        return
    
    confirm = input(f"Are you sure you want to remove '{item_name}'? (y/n): ").lower()
    
    if confirm == "y":
        del inventory[item_name]
        print(f"'{item_name}' removed from inventory successfully!")
    else:
        print("Item removal cancelled.")

if __name__ == "__main__":
    main()