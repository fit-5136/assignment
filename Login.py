from User_data import *


def login(list_of_user):

    login_input = []
    input_account = input("--- Please enter your Employee ID: ")
    login_input.append(input_account)
    input_password = input("--- Please enter your Password: ")
    login_input.append(input_password)

    count_valid_id = 0
    for user in list_of_user:
        if user.get_emp_id() == login_input[0]:
            if user.get_emp_password() == login_input[1]:
                count_valid_id += 1
                print("*** Login Successful ***")
                return user
            else:
                count_valid_id += 1
                print("!!! [Error] Incorrect Password !!!")
                return login(list_of_user)
        else:
            if user.get_emp_id() == list_of_user[-1].get_emp_id() and count_valid_id == 0:
                print("!!! [Error] Invalid Employee ID !!!")
                return login(list_of_user)


def select_store(user):
    while True:
        try:
            input_value = input("--- Please enter a store number: ")
            if 1 <= int(input_value) <= 10:
                store_no = int(input_value)
                user.set_emp_store_no(store_no)
                print("*** Selection Successful ***")
                print("*** Store " + str(user.get_emp_store_no()) + " is selected ***")
                break
            else:
                print("!!! [Error] Please enter a number between 1 and 10 !!!")
        except ValueError:
            print("!!! [Error] Please enter a number between 1 and 10 !!!")


if __name__ == '__main__':
    user_list = load_user()
    current_user = login(user_list)
    print(current_user)
    if current_user.get_emp_type() == "Owner":
        select_store(current_user)





