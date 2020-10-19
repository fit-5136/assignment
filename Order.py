class NewItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def print_data(self):
        print(self.name + '  ' + str(self.quantity) + '  ' + str(self.price))

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity


class Order:
    def __init__(self, store_id, order_id, staff_id, date, time, status, customer, phone):
        self.store_id = store_id
        self.order_id = order_id
        self.staff_id = staff_id
        self.date = date
        self.time = time
        self.status = status
        self.customer = customer
        if phone == "None":
            self.phone = []
        else:
            self.phone = phone
        self.item_list = {}
        self.num_of_items = 0
        self.total_price = 0

    def add_item(self, name, quantity, price):
        self.item_list[name] = NewItem(name, quantity, price)
        self.num_of_items += 1
        self.total_price += price

    def get_customer(self):
        return self.customer

    def get_date(self):
        return self.date

    def get_num_of_items(self):
        return self.num_of_items

    def get_order_id(self):
        return self.order_id

    def get_phone(self):
        return self.order_id

    def get_staff_id(self):
        return self.staff_id()

    def get_status(self):
        return self.status

    def get_store_id(self):
        return self.store_id

    def get_time(self):
        return self.time

    def get_total_price(self):
        return self.total_price

    def print_item_list(self):
        for i in self.item_list.keys():
            self.item_list[i].print_data()
        print(self.num_of_items)
        print(self.total_price)
        print("_______________")

    def get_item_list(self):
        return self.item_list

    def set_customer(self, customer):
        self.customer = customer

    def set_date(self, date):
        self.date = date

    def set_order_id(self, order_id):
        self.order_id = order_id

    def set_phone(self, phone):
        self.phone = phone

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id

    def set_status(self, status):
        self.status = status

    def set_store_id(self, store_id):
        self.store_id = store_id

    def set_time(self, time):
        self.time = time


def load_orders():
    data = open("Orders.txt", "r")
    lines = data.readlines()
    data.close()

    list_of_order = []
    for line in lines:
        order = line.split("/")
        [store_id, order_id, staff_id, date, time, status, customer, phone] = order[0:8]
        new_order = Order(store_id, order_id, staff_id, date, time, status, customer, phone)
        for i in range(int(order[-2])):
            [name, quantity, price] = order[7+(3*i+1):7+(3*i+4)]
            new_order.add_item(name, int(quantity), int(price))
        list_of_order.append(new_order)
    return list_of_order


if __name__ == '__main__':
    list_of_order = load_orders()
    list_of_order[1].print_item_list()





