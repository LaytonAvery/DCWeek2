# Grocery App
# You are responsible for creating an app that manages groceries. Your groceries are characterized by Shopping Lists which can contain grocery items. Here are the features you need to implement:

# You need to ask the user for the input.
# A user should be able to create a shopping list. A shopping list consists of a title and address. Example = Fiesta, Walmart, Sams Club, Costco, Randalls etc

# A user should be able to add multiple shoppings lists

# Give user an option to display the list

# A user should be able to add a grocery items to a particular shopping list. A grocery item consists of a title, price, quantity. Example Milk, Cookies, Paper, Napkins, Soda, Chips etc

# Fiesta

# Milk, Soda, Fish
# try to print("+++++++++++++++++")
# Walmart

# Paper, Napkins, Plate, Chips

# Sams Club

# Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey


# You are going to continue working on the Grocery App and add the following features to the app.

# User should be able to delete a store
# User should be able to delete an item from a particular store
# Are there places in your app where you need to handle exceptions?
# What are different unit tests you are going to implement for your Grocery App application
# How can you create separate your different classes into separate modules?


stores = []
item = []

print("Hello! Time to make a grocery list!")


def menu():
    print("Menu:")
    print("-----------------------")
    print("Press 1 to add a store.")
    print("Press 2 to add a store address.")
    print("Press 3 to add an item.")
    print("Press 4 to delete an item.")
    print("Press 5 to delete a store.")
    print("Press 6 to view all lists.")
    print("Press q to quit.")


menu()


class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_stores():
        for store in Stores:
            print(f'{store.name}--{store.address}')


class Item:
    def __init__(self, item, price, quantity):
        self.item = []
        self.price = ""
        self.quantity = ""
        return (self.item, self.price, self.quantity)


class List:
    def __init__(self)
    # figure out what to add here

    def display_all_lists():
        for index in range(0, len(lists)+1):
            list_items = lists[index]
            print(f"Here is your list {list_items}")

    def add_item():
        # attempting to display stores to add item to store
        list_item = input("To which list would you like to add an item? ")
        for index in range(0, len(stores))
        store = stores[index]
        print(f"{index+1}--{store.name}--{store.address}")

    def delete_items():
        delete_item = int(
            input("Enter the item number you would like to delete: "))
        del item[delete_item - 1]

    def delete_stores():
        delete_store = int(
            input("Enter the number of the store that you'd like to delete: "))
        del store[delete_store - 1]


while True:
    selection = input("Enter selection: ")

    if selection == "1":
        title = input("What store would you like to visit? ")
        Store(title)

    elif selection == "2":
        address = input("What is the address of this store? ")
        Store(address)

    elif selection == "3":
        List(add_item)

    elif selection == "4":
        delete_items()  # not defined?

    elif selection == "5":
        delete_stores()  # not defined?

    elif selection == "6":
        for items in List:
            display_all_lists()

    elif selection == "q":
        break

print("Thank you for using the grocery app!")
