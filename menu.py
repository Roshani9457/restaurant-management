#Roshani
# menu.py
from exceptions import CustomException, InvalidMenuItemError, InsufficientQuantityError

class MenuItem:
    def __init__(self, name, price, quantity):   #initialize menu
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu:
    def __init__(self):        #Initialize menu with empty dictionary of items.
        self.items = {}

    def add_item(self, name, price, quantity):    #add item to menu
        if name in self.items:
            raise CustomException("Item" + name + "already exists.")   
        self.items[name] = MenuItem(name, price, quantity)
        self.write_menu_to_file()      

    def update_item(self, name, price, quantity):    #update price and quantity of item
        if name not in self.items:
            raise InvalidMenuItemError("Item" + name + "does not exist.")      #raise InvalidMenuItemError
        self.items[name].price = price
        self.items[name].quantity = quantity
        self.write_menu_to_file()           

    def delete_item(self, name):       #delete item from menu
        if name not in self.items:
            raise InvalidMenuItemError("Item" + name + "does not exist.")     
        del self.items[name]
        self.write_menu_to_file()                

    def display_menu(self):        #display menu
        for item in self.items.values():
            print("Name:" + item.name + ", Price:" + str(item.price) + ", Quantity:" + str(item.quantity))

    def read_menu_from_file(self):      #read menu items from a file
        try:
            with open('menu.txt', 'r') as file:
                for line in file:
                    name, price, quantity = line.strip().split(',')
                    self.items[name] = MenuItem(name, float(price), int(quantity))
        except FileNotFoundError:
            pass

    def write_menu_to_file(self):        #Save menu items to a file
        with open('menu.txt', 'w') as file:
            for item in self.items.values():
                file.write(item.name + "," +  str(item.price) + "," + str(item.quantity) + "\n")

