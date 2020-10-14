class User:

    def __init__(self, emp_id, emp_name, emp_email, emp_password, emp_type, emp_tfn, emp_street, emp_city, emp_state, emp_postal, emp_phone, emp_store_no):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_email = emp_email
        self.emp_password = emp_password
        self.emp_type = emp_type
        self.emp_tfn = emp_tfn
        self.emp_street = emp_street
        self.emp_city = emp_city
        self.emp_state = emp_state
        self.emp_postal = emp_postal
        self.emp_phone = emp_phone
        self.emp_store_no = emp_store_no

    def set_emp_id(self, emp_id):
        self.emp_id = emp_id

    def set_emp_name(self, emp_name):
        self.emp_name = emp_name

    def set_emp_email(self, emp_email):
        self.emp_email = emp_email

    def set_emp_password(self, emp_password):
        self.emp_password = emp_password

    def set_emp_type(self, emp_type):
        self.emp_type = emp_type

    def set_emp_tfn(self, emp_tfn):
        self.emp_tfn = emp_tfn

    def set_emp_street(self, emp_street):
        self.emp_street = emp_street

    def set_emp_city(self, emp_city):
        self.emp_city = emp_city

    def set_emp_state(self, emp_state):
        self.emp_state = emp_state

    def set_emp_postal(self, emp_postal):
        self.emp_postal = emp_postal

    def set_emp_phone(self, emp_phone):
        self.emp_phone = emp_phone

    def set_emp_store_no(self, emp_store_no):
        self.emp_store_no = emp_store_no

    def get_emp_id(self):
        return self.emp_id

    def get_emp_name(self):
        return self.emp_name

    def get_emp_email(self):
        return self.emp_email

    def get_emp_password(self):
        return self.emp_password

    def get_emp_type(self):
        return self.emp_type

    def get_emp_tfn(self):
        return self.emp_tfn

    def get_emp_street(self):
        return self.emp_street

    def get_emp_city(self):
        return self.emp_city

    def get_emp_state(self):
        return self.emp_state

    def get_emp_postal(self):
        return self.emp_postal

    def get_emp_phone(self):
        return self.emp_phone

    def get_emp_store_no(self):
        return self.emp_store_no


def load_user():
    data = open("Employee Info.txt", "r")
    lines = data.readlines()
    data.close()

    list_of_user = []
    for line in lines:
        emp = line.split("/")
        user = User(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], emp[10], emp[11])
        list_of_user.append(user)
    return list_of_user



