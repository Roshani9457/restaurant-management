#Roshani
# order.py
from exceptions import CustomException, InvalidMenuItemError, InsufficientQuantityError
import menu
class Order:
    def __init__(self, menu):       #initialize order
        self.menu = menu
        self.items = {}

    def add_item(self, name, quantity):      #add item 
        if name not in self.menu.items:
            raise InvalidMenuItemError("Item" + name + "is not on the menu.")        #raise InvalidMenuItemError
        if self.menu.items[name].quantity < quantity:
            raise InsufficientQuantityError("Not enough quantity for" + name)         #raise InsufficientQuantityError
        self.menu.items[name].quantity -= quantity
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = menu.MenuItem(name, self.menu.items[name].price, quantity)

    def calculate_total(self,tax_rate,discount_rate):      #calculate total
        sub_total=sum(item.price * item.quantity for item in self.items.values())
        tax=sub_total*tax_rate
        discount=sub_total*discount_rate
        total=sub_total+tax-discount
        return total 

    def generate_receipt(self):     #generate receipt
        total = self.calculate_total(0.08,0.15)        
        receipt = "\n".join([item.name + " x " + str(item.quantity) + " : " + str(item.price) for item in self.items.values()])
        receipt += "\nTotal: " + str(total) + "\n"
        return receipt

    def read_orders_from_file(self):       #Load previous orders from a file
        try:
            with open('orders.txt', 'r') as file:
                # Process stored orders if needed
                pass
        except FileNotFoundError:
            pass

    def write_orders_to_file(self):           #save order to file
        try:
            with open('orders.txt', 'a+') as file:
                for item in self.items.values():
                    file.write(item.name + "," +  str(item.price) + "," + str(item.quantity) + "\n")
        except FileNotFoundError:
            pass
 
