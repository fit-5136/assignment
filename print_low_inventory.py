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
    item_list = list_of_inventory[select_store - 1].get_item_list()

    low_inventory_list = {}
    for item in item_list.keys():
        if item_list[item].get_quantity() < 10:
            low_inventory_list[item_list[item].get_name()] = item_list[item].get_quantity()

    for x, y in low_inventory_list.items():
        print(x, y)


if __name__ == '__main__':
    low_inventory_report()


