from Order import *
from datetime import date
from datetime import datetime


def revenue_report():
    list_of_order = load_orders()

    today = date.today()
    date1 = datetime.strptime(str(today), "%Y-%m-%d")

    list_of_revenue = {'store_1': 0, 'store_2': 0, 'store_3': 0, 'store_4': 0, 'store_5': 0, 'store_6': 0, 'store_7': 0,
                       'store_8': 0, 'store_9': 0, 'store_10': 0}

    for order in list_of_order:
        date2 = order.get_date()
        date3 = datetime.strptime(str(date2), "%d-%m-%Y")
        if date3.month + 1 == date1.month:
            list_of_revenue['store_' + order.get_store_id()] += order.get_total_price()

    print(list_of_revenue)


if __name__ == '__main__':
    revenue_report()


