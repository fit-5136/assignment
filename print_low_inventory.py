from Inventory import *


def low_inventory_report():
    while True:
        try:
            input_value = input("--- Please enter a store number: ")
            if 1 <= int(input_value) <= 10:
                select_store = int(input_value)
                print("*** Selection Successful ***")
                print("*** Store " + str(select_store) + " is selected ***")
                break
            else:
                print("!!! [Error] Please enter a number between 1 and 10 !!!")
        except ValueError:
            print("!!! [Error] Please enter a number between 1 and 10 !!!")

    list_of_inventory = load_inventory()
    low_inventory_list = []

    for inventory in list_of_inventory:
        if inventory.get_quantity() < 10 and inventory.get_store_id() == select_store:
            low_inventory_list.append((inventory.get_name(), inventory.get_quantity()))
    print(list_of_inventory)


if __name__ == '__main__':
    low_inventory_report(1)


