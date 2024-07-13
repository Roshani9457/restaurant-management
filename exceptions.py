#Roshani
# exceptions.py

class CustomException(Exception):   #base class for other custom exceptions
    pass

class InvalidMenuItemError(CustomException):
    #Raised when the menu item is invalid.
    pass

class InsufficientQuantityError(CustomException):
    #Raised when there is not enough quantity of a menu item.
    pass
