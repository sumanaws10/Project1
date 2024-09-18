

def display_menu(menu):
    print("Welcome to our cafe!\n")
    
    for category, items in menu.items():
        print(f"{category.title()}:")
        for item, price in items.items():
            print(f"  {item.title()} €{price}")
        print()  
    
# display_menu(menu)

def take_order(menu):
    display_menu(menu)
    order = {}
    total_cost = 0
    print("Please place your order. Type 'done' when finished.\n")

    while True:
        item = input("Enter an item from the menu: ")
        
        if item == 'done':
            break
        
        # Check if the item is in the menu
        found = False
        for category in menu.values():
            if item in category:
                found = True
                quantity = int(input(f"How many {item.capitalize()} would you like? "))
                price = category[item]
                order[item] = quantity
                total_cost += price * quantity
                print(f"Added {quantity} x {item.capitalize()} to your order. Subtotal: ${total_cost}\n")
                break
        
        if not found:
            print("Sorry, that item is not on the menu. Please try again.\n")
    
    return order, total_cost

# Example usage:
# order, total = take_order(menu)
# print("\nYour order summary:")
# for item, quantity in order.items():
#     print(f"{quantity} x {item.capitalize()}")
# print(f"Total Cost: ${total}")




