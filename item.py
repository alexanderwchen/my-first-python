class Item:
    def __init__(self, name, price, vendor, wasYummy):
        self.name = name
        self.price = price
        self.vendor = vendor
        self.isYummy = wasYummy

    def display(self):
        print("Name: " + self.name)
        print("Price: " + str(self.price))
        print("Vendor: " + self.vendor)
        print("Yummy?:"),
        if self.isYummy:
            print("Yes!")
        else:
            print("No!")


def add_prices(item1, item2):
    total_price = item1.price + item2.price
    return total_price


def displayAll(args):
    counter = 1
    for x in args:
        print("Item " + str(counter))
        x.display()
        print("\n")
        counter += 1

item1 = Item("Coffee", 100, "Alex", True)
item2 = Item("Tea", 123456, "Alexander", False)

items = [item1, item2]

print("MENU\n")
displayAll(items)

order_choice = raw_input("Please enter the item # you'd like to order: ")
if all(char.isdigit() for char in order_choice):
    if 0 < int(order_choice) <= len(items):
        print("Good Choice. I love " + items[int(order_choice)-1].name.lower() + " too!")
        print("That will be $" + str(items[int(order_choice)-1].price))

else:
    print("INVALID INPUT")
