class Item:
    def __init__(self, item_id, name, price, item_type, quantity, date_inventory_added, monthly_sales=0):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.item_type = item_type
        self.quantity = quantity
        self.date_inventory_added = date_inventory_added
        self.monthly_sales = monthly_sales

    def add_monthly_sale(self, quantity):
        self.monthly_sales += quantity

    def get_date_inventory_added(self):
        return self.date_inventory_added

    def get_item_id(self):
        return self.item_id

    def get_monthly_sales(self):
        return self.monthly_sales

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_type(self):
        return self.item_type

    def print_item(self):
        print(self.name + "   " + str(self.price) + "  " + str(self.quantity) + "   " + self.date_inventory_added)

    def set_date_inventory_added(self, date_inventory_added):
        self.date_inventory_added = date_inventory_added

    def set_item_id(self, item_id):
        self.item_id = item_id

    def set_monthly_sales(self, quantity):
        self.monthly_sales = quantity

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_type(self, type):
        self.item_type = type


class Inventory:
    def __init__(self, store_id):
        self.store_id = store_id
        self.item_list = {}

    def add_item(self, item_id, name, price, item_type, quantity, date_inventory_added, monthly_sales=0):
        if name not in self.item_list.keys():
            self.item_list[name] = Item(item_id, name, price, item_type, quantity, date_inventory_added, monthly_sales)
        else:
            print('Item already exists')

    def get_item_list(self):
        return self.item_list

    def print_item_list(self):
        for i in self.item_list.keys():
            self.item_list[i].print_item()

    def update_item(self, name, quantity, date_inventory_added):
        self.item_list[name].set_quantity(self.item_list[name].get_quantity() + quantity)
        self.item_list[name].set_date_invetory(date_inventory_added)


def load_inventory():
    list_of_inventory = []
    for i in range(0, 10):
        list_of_inventory.append(Inventory(i + 1))

    data = open("Inventory.txt", "r")
    lines = data.readlines()
    data.close()

    for line in lines:
        line = line.strip("\n")
        item = line.split("/")
        [store_id, item_id, name, price, item_type, quantity, date_inventory_added, monthly_sales] = item
        if store_id == "0":
            for i in range(0, 10):
                list_of_inventory[i].add_item(item_id, name, float(price), item_type, int(quantity),
                                              date_inventory_added, monthly_sales)
        else:
            list_of_inventory[int(store_id) - 1].add_item(item_id, name, float(price), item_type, int(quantity),
                                                          date_inventory_added, monthly_sales)

    return list_of_inventory


if __name__ == '__main__':
    list_of_inventory = load_inventory()
    a = list_of_inventory[3 - 1].get_item_list()
    b = list_of_inventory[4-1].get_item_list()
    b["coffee1"].set_quantity(3)
    print(b["coffee1"].get_quantity())
    print(a["coffee1"].get_quantity())
