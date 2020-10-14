from Inventory import *
class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.customer_phone = ""


def create_order(account_type, store_id, staff_name):
    print("    ********** Welcome "+staff_name+" **********    ")
    print("--- Account type: "+account_type)
    print("--- Store ID: "+str(store_id))
    print("\n")
    print("\n")

    print(">>You are currently at Create Orders page")
    print("\n")
    print("--- Please enter the option (1-4)")
    print("1. General orders")
    print("2. Advance orders")
    print("3. Delete")
    print("4. back to MANAGE ORDER")
    print("\n")

    x = 0
    while x == 0:
        option = input("--- Enter your option:")

        if option == "1":
            create_general_order(account_type, store_id, staff_name)
            x = 1
        elif option == "2":
            create_advance_order(account_type, store_id, staff_name)
            x = 1
        elif option == "3":
            # manage_order()
            x = 1
        elif option == "4":
            # manage_order()
            x = 1
        else:
            print("!!! [ERROR] Please enter right number !!!")


def create_general_order(account_type, store_id, staff_name):
    print("    ********** Welcome " + staff_name + " **********    ")
    print("--- Account type: " + account_type)
    print("--- Store ID: " + str(store_id))
    print("\n")
    print("\n")

    print(">>You are currently at Create General Orders page")
    print("\n")

    x = 0
    while x == 0:
        option = input("--- Customer name:")

        if option is None:
            print("!!! [ERROR] Customer name cannot be null !!!")
        else:
            customer_name = option
            x = 1

    print("--- Please enter the option (1-2)")
    print("1. Next")
    print("2. Delete")
    print("\n")

    y = 0
    while y == 0:
        option1 = input("--- Enter your option:")

        if option1 == "1":
            general_order(account_type, store_id, staff_name, customer_name)
            y = 1
        elif option1 == "2":
            # manage_order()
            y = 1
        else:
            print("!!! [ERROR] Please enter right number !!!")


def general_order(account_type, store_id, staff_name, customer_name):
    order = Order(customer_name)
    print("    ********** Welcome " + staff_name + " **********    ")
    print("--- Account type: " + account_type)
    print("--- Store ID: " + str(store_id))
    print("\n")
    print("\n")

    print(">>You are currently at Create General Orders page")
    print("\n")

    x = 0
    while x == 0:
        if len(order.items) != 0:
            count = 1
            for item in order.items:
                print("====================")
                print("Item_"+str(count)+" Name "+item[0])
                print("Item_"+str(count)+" Quantity "+str(item[1]))
                count+=1
        print("\n")

        print("--- Please enter the option (1-3)")
        print("1. Confirm")
        print("2. Add item")
        print("3. Delete")
        print("\n")

        option = input("--- Enter your option:")

        if option == "1":
            # add_order()
            x = 1
        elif option == "2":
            add_item(account_type, store_id, staff_name, order)
        elif option == "3":
            #delete_order()
            x = 1
        else:
            print("!!! [ERROR] Please enter right number !!!")


def add_item(account_type, store_id, staff_name, order):
    print("    ********** Welcome " + staff_name + " **********    ")
    print("--- Account type: " + account_type)
    print("--- Store ID: " + str(store_id))
    print("\n")
    print("\n")

    print(">>You are currently at Add Item page")
    print("\n")

    x = 0
    while x == 0:
        item_name = input("Item Name: ")
        if item_name in Inventory.name:
            x = 1
        else:
            print("!!! [ERROR] Item NOT Found !!!")

    y = 0
    while y == 0:
        item_quantity = input("Item Quantity: ")
        if int(item_quantity) > 0:
            y = 1
        else:
            print("!!! [ERROR] Invalid Number !!!")

    order.items.append((item_name, int(item_quantity)))

    z = 0
    while z == 0:
        option = input("--- Enter your option:")

        if option == "1" | option == "2":
            z = 1
        else:
            print("!!! [ERROR] Please enter right number !!!")


def create_advance_order(account_type, store_id, staff_name):
    print("    ********** Welcome " + staff_name + " **********    ")
    print("--- Account type: " + account_type)
    print("--- Store ID: " + str(store_id))
    print("\n")
    print("\n")

    print(">>You are currently at Create Advance Orders page")
    print("\n")

    x = 0
    while x == 0:
        option = input("--- Customer name: ")

        if option is None:
            print("!!! [ERROR] Customer name cannot be null !!!")
        else:
            customer_name = option
            x = 1

    y = 0
    while y == 0:
        option1 = input("--- Customer phone: ")

        if option1 is None:
            print("!!! [ERROR] Invalid phone number !!!")
        #elif option1  is invalid
        else:
            customer_phone = option1
            y = 1

    print("--- Please enter the option (1-2)")
    print("1. Next")
    print("2. Delete")
    print("\n")

    z = 0
    while z == 0:
        option2 = input("--- Enter your option:")

        if option2 == "1":
            advance_order(account_type, store_id, staff_name, customer_name, customer_phone)
            z = 1
        elif option2 == "2":
            # manage_order()
            z = 1
        else:
            print("!!! [ERROR] Please enter right number !!!")


def advance_order(account_type, store_id, staff_name, customer_name, customer_phone):
    order = Order(customer_name)
    order.customer_phone = customer_phone
    print("    ********** Welcome " + staff_name + " **********    ")
    print("--- Account type: " + account_type)
    print("--- Store ID: " + str(store_id))
    print("\n")
    print("\n")

    print(">>You are currently at Create Advance Orders page")
    print("\n")

    x = 0
    while x == 0:
        if order.items.length != 0:
            count = 1
            for item in order.items:
                print("====================")
                print("Item_" + str(count) + " Name " + item[0])
                print("Item_" + str(count) + " Quantity " + str(item[1]))
                count += 1
        print("\n")

        print("--- Please enter the option (1-3)")
        print("1. Confirm")
        print("2. Add item")
        print("3. Delete")
        print("\n")

        option = input("--- Enter your option:")

        if option == "1":
            # add_order()
            x = 1
        elif option == "2":
            add_beans(account_type, store_id, staff_name, order)
        elif option == "3":
            #delete_order()
            x = 1
        else:
            print("!!! [ERROR] Please enter right number !!!")


def add_beans(account_type, store_id, staff_name, order):
    print("    ********** Welcome " + staff_name + " **********    ")
    print("--- Account type: " + account_type)
    print("--- Store ID: " + str(store_id))
    print("\n")
    print("\n")

    print(">>You are currently at Add Item page")
    print("\n")

    x = 0
    while x == 0:
        item_name = input("Item Name: ")
        if item_name is not "roast coffee beans":
            print("!!! [ERROR] !!!")
        else:
            x = 1

    y = 0
    while y == 0:
        item_quantity = input("Item Quantity: ")
        if int(item_quantity) > 0:
            y = 1
        else:
            print("!!! [ERROR] Invalid Number !!!")

    order.items.append((item_name, int(item_quantity)))

    z = 0
    while z == 0:
        option = input("--- Enter your option:")

        if option == "1" | option == "2":
            z = 1
        else:
            print("!!! [ERROR] Please enter right number !!!")


#def delete_order():


if __name__ == '__main__':
    type = "staff"
    name = "Kelly Atkins"
    id = 7
    create_order(type,id,name)