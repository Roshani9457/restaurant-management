#Roshani
# restaurant.py

from menu import Menu
from order import Order
from exceptions import CustomException, InvalidMenuItemError, InsufficientQuantityError

menu = Menu()        #create object of class Menu
menu.read_menu_from_file()
order = Order(menu)       #create instance

while next!='no':
    print("1. Display Menu")
    print("2. Add Item to Menu")
    print("3. Update Item in Menu")
    print("4. Delete Item from Menu")
    print("5. Place Order")
    print("6. View Order")
    print("7. Generate Receipt")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        # Add a new item to the menu
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        menu.add_item(name, price, quantity)           
    elif choice == '2':
        # Update an existing item in the menu
        name = input("Enter item name to update: ")
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))
        menu.update_item(name, price, quantity)          
    elif choice == '3':
        # Delete an item from the menu
        name = input("Enter item name to delete: ")
        menu.delete_item(name)           
    elif choice == '4':
            # Display the current menu
        menu.display_menu()        
    elif choice == '5':
            # Place a new order
        while True:
            item_name = input("Enter item name to order (or 'done' to finish): ")
            if item_name == 'done':
                break
            quantity = int(input("Enter quantity: "))
            order.add_item(item_name, quantity)      
    elif choice == '6':
            # Generate a receipt for the current order
        print(order.generate_receipt())     
        order.write_orders_to_file() 
    elif choice == '7':
        print('Exit')
        break   
    else:
        print("Invalid choice.")
