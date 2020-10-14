from Order import *
import Order
from datetime import date
from datetime import datetime


def print_2_report():
    list_of_order = Order.load_orders()

    today = date.today()
    date1 = datetime.strptime(str(today), "%Y-%m-%d")

    list_of_coffee = {'store_1':0,'store_2':0,'store_3':0,'store_4':0,'store_5':0,'store_6':0,'store_7':0,'store_8':0,'store_9':0,'store_10':0}

    for order in list_of_order:
        date2 = order.get_date()
        date3 = datetime.strptime(str(date2), "%d-%m-%Y")
        if date3.month + 1 == date1.month:
            items = order.get_item_list().keys()
            for item in items:
                if item == "coffee":
                    if list_of_coffee['store_'+order.get_store_id()] == 0:
                        list_of_coffee['store_'+order.get_store_id()] = 1
                    else:
                        list_of_coffee['store_'+order.get_store_id()] += 1

    print(list_of_coffee)

    list_of_beans = {'store_1':0,'store_2':0,'store_3':0,'store_4':0,'store_5':0,'store_6':0,'store_7':0,'store_8':0,'store_9':0,'store_10':0}

    for order in list_of_order:
        date4 = order.get_date()
        date5 = datetime.strptime(str(date4), "%d-%m-%Y")
        if date5.month + 1 == date1.month:
            items = order.get_item_list().keys()
            for item in items:
                if item == "roast coffee beans":
                    if list_of_beans['store_'+order.get_store_id()] == 0:
                        list_of_beans['store_'+order.get_store_id()] = 1
                    else:
                        list_of_beans['store_'+order.get_store_id()] += 1

    print(list_of_beans)


if __name__ == '__main__':
    print_2_report()