# Student name: Changsheng Deng
# Student id: 30170893
# Start date: 5.10.2020
# Last modified date: 5.10.2020


class Store:

    def __init__(self, store_id, street, city, suburb, postal, phone):
        self.store_id = store_id
        self.street = street
        self.city = city
        self.suburb = suburb
        self.postal = postal
        self.phone = phone

    def get_city(self):
        return self.city

    def get_postal(self):
        return self.postal

    def get_phone(self):
        return self.phone

    def get_store_id(self):
        return self.store_id

    def get_street(self):
        return self.street

    def get_suburb(self):
        return self.suburb

    def set_city(self, city):
        self.city = city

    def set_postal(self, postal):
        self.postal = postal

    def set_phone(self, phone):
        self.phone = phone

    def set_store_id(self, store_id):
        self.store_id = store_id

    def set_street(self, street):
        self.street = street

    def set_suburb(self, suburb):
        self.suburb = suburb


def load_stores():
    data = open("Stores.txt", "r")
    lines = data.readlines()
    data.close()

    list_of_store = {}
    for line in lines:
        store = line.split("/")
        [store_id, street, city, suburb, postal, phone] = store
        new_store = Store(store_id, street, city, suburb, postal, phone)
        list_of_store[str(store_id)] = new_store
    return list_of_store





