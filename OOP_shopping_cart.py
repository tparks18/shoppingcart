class Cart:
    def __init__(self):  # represents empty cart
        self.total = 0  # total price of items in the cart before shopping
        self.items = {}  # initalizing empty dictionary
        # super().__init__(self, ) - i didn't know where to put this 😅


class Item(Cart):
    # represents aspects of the groceries, specific to the item
    def __init__(self, qty, name, price):  # initializes attributes of the parent class
        self.qty = qty
        self.name = name
        self.price = price

    def add_item(self):
        self.total += qty*price  # calculates price
        self.items.append(Item)  # adds item to cart
        return self.total, self.items

    def remove_item(self):
        Cart.remove(Item)
        return self.total, self.items

    def show_cart(self):
        print(
            f'You have {self.qty} {self.name} worth {self.total} in your shopping cart')


print("Shopping Cart Actions")
print("1: Add item")
print("2: Remove item")
print("3: View basket ")
print("0: Stop shopping")


def shoppingCart():
    action = int(input('What would you like to do?'))

    while action != 0:
        if action == 1:
            Item = input("What are you getting? ")
            qty = int(input("How many items? "))
            shopping_cart[Item] = qty
        elif action == 2:
            item = input("What are you deleting? ")
            del(Cart[Item])
        elif action == 3:
            return Cart
        elif action != 0:
            return("Please select a valid action!")
        else:
            return("You are ready for checkout. Your total is {self.total}")
