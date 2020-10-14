class Item:
    def __init__(self, item_id, name, price, quantity, date_inventory_added):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.date_inventory_added = date_inventory_added

    def get_date_inventory_added(self):
        return self.date_inventory_added

    def get_item_id(self):
        return self.item_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_date_inventory_added(self, date_inventory_added):
        self.date_inventory_added = date_inventory_added

    def set_item_id(self, item_id):
        self.item_id = item_id

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity


class Inventory:
    def __init__(self, store_id):
        self.store_id = store_id
        self.item_list = {}

    def add_item(self, item_id, name, price, quantity, date_inventory_added):
        if name not in self.item_list.keys():
            self.item_list[name] = Item(item_id, name, price, quantity, date_inventory_added)
        else:
            print('Item already exists')

    def update_item(self, name, quantity, date_inventory_added):
        self.item_list[name].set_quantity(self.item_list[name].get_quantity() + quantity)
        self.item_list[name].set_date_invetory(date_inventory_added)

    def get_item_list(self):
        return self.item_list


if __name__ == '__main__':
    I = Inventory(1)
    I.add_item(1, 'xsc', 2, 23, 45)
    I.add_item(1, 'xsc', 2, 23, 45)
    I.add_item(2, 'ssc', 2, 24, 25)
    print(I.get_item_list().keys())
    print(I.get_item_list()['xsc'].get_quantity())


