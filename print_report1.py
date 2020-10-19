from Inventory import *


def print_report1(option, store_id):
    list_of_inventory = load_inventory()
    item_list = list_of_inventory[store_id - 1].get_item_list()

    monthly_food_sales = {}
    monthly_coffee_sales = {}
    for item in item_list.keys():
        if item_list[item].get_type() == "food":
            monthly_food_sales[item_list[item].get_name()] = int(item_list[item].get_monthly_sales())
        elif item_list[item].get_type() == "coffee":
            monthly_coffee_sales[item_list[item].get_name()] = int(item_list[item].get_monthly_sales())
    top_monthly_food_sales = sorted(monthly_food_sales.items(), key=lambda i: i[1], reverse=True)[:10]
    top_monthly_coffee_sales = sorted(monthly_coffee_sales.items(), key=lambda i: i[1], reverse=True)[:10]
    if option == 1:
        for i in top_monthly_food_sales:
            print(i[0] + "    " + str(i[1]))
    elif option == 2:
        for i in top_monthly_coffee_sales:
            print(i[0] + "    " + str(i[1]))


if __name__ == '__main__':
    print_report1(2, 3)
