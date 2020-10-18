from Order import *
from datetime import *


def print_report2(store_id):
    list_of_order = load_orders()
    local_date = date.today()
    revenue = [0, 0, 0, 0, 0, 0, 0]

    for order in list_of_order:
        if order.get_store_id() == str(store_id):
            order_date = datetime.strptime(order.get_date(), '%d-%m-%Y')
            if order_date.year == local_date.year and order_date.month == local_date.month - 1:
                revenue[order_date.isoweekday()-1] += int(order.get_total_price())
    print("The top sale day is weekday: " + str(revenue.index(max(revenue))+1) + ", revenue: " + str(max(revenue)))


if __name__ == '__main__':
    print_report2(3)

