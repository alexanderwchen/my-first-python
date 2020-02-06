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


def add_prices(i1, i2):
    total_price = i1.price + i2.price
    return total_price


def displayAll(args):
    counter = 1
    for x in args:
        print("Item " + str(counter))
        x.display()
        print("\n"),
        counter += 1

item1 = Item("Coffee", 100, "Alex", True)
item2 = Item("Tea", 123456, "Alexander", False)

cost = 0
keep_running = True

items = [item1, item2]


while keep_running:

    print("MENU\n")
    displayAll(items)

    order_choice = raw_input("Please enter the item # you\'d like to order: ")
    if all(char.isdigit() for char in order_choice) and 0 < int(order_choice) <= len(items):
        cost += items[int(order_choice)-1].price
        print("Good Choice. I love " + items[int(order_choice)-1].name.lower() + " too!")
        print("That will be $" + str(items[int(order_choice)-1].price))

        to_continue = raw_input("Would you like to order anything else? (Y/N): ")
        if to_continue != "Y" and to_continue != "y":
            keep_running = False

    else:
        print("INVALID INPUT")

print("Thank you for visiting. You're total cost was: $" + str(cost))
print("Good Bye!")