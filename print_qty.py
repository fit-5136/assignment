from Order import *
from Inventory import *
from datetime import date
from datetime import datetime


def food_qty_report():
    list_of_order = load_orders()
    list_of_inventory = load_inventory()
    inventory_list = list_of_inventory[0].get_item_list()

    today = date.today()
    date1 = datetime.strptime(str(today), "%Y-%m-%d")

    list_of_food = {'store_1': 0, 'store_2': 0, 'store_3': 0, 'store_4': 0, 'store_5': 0, 'store_6': 0, 'store_7': 0,
                    'store_8': 0, 'store_9': 0, 'store_10': 0}

    for order in list_of_order:
        date2 = order.get_date()
        date3 = datetime.strptime(str(date2), "%d-%m-%Y")
        if date3.month + 1 == date1.month:
            items = order.get_item_list()
            for item in items:
                if inventory_list[item].get_type() == "food":
                    list_of_food['store_' + order.get_store_id()] += items[item].get_quantity()

    for x, y in list_of_food.items():
        print(x, y)


if __name__ == '__main__':
    food_qty_report()

