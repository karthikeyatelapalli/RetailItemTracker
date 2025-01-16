
# Retail items  
'''
A class named Retail_Item is defined in the code. The three characteristics for this class are item_name, amount, and price.
When an object of the Retail_Item class is formed, the init method initializes these properties. The object's text 
representation is the result of the str function. The user is prompted to input the names, quantities, and prices
of two products in the main function. After that, two Retail_Item instances are created, and a list of the products 
is printed.
'''

class Retail_Item:
    def __init__(self, item_name, amount, price):
        self.__item_type = item_name
        self.__amount = amount
        self.__price = price
    
    def __str__(self):
        return f"{self.__item_type.ljust(10)}{str(self.__amount).rjust(11)}" \
               f"{'$'.rjust(11)}" \
               f"{'{:.2f}'.format(self.__price)}"


def main():
    print()
    item1_name = input("Name of item 1: ")
    item1_amount = int(input("Amount of item 1: "))
    item1_price = float(input("Price of item 1: "))
    item1 = Retail_Item(item1_name, item1_amount, item1_price)
    print()
    item2_name = input("Name of item 2: ")
    item2_amount = int(input("Amount of item 2: "))
    item2_price = float(input("Price of item 2: "))
    item2 = Retail_Item(item2_name, item2_amount, item2_price)
    print()
    print("Here is a summary of the items you added:")
    print("Item".ljust(10) + "Amount".rjust(12) + "Price".rjust(15))
    print("-" * 38)
    print(str(item1))
    print(str(item2))


if __name__ == "__main__":
    main()
