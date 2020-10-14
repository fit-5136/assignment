from Login import *
from Logout import *

def display_home_menu(user):
    if user.get_emp_type() == "Owner":
        print("    ********** Welcome " + user.get_emp_name() + " **********    ")
        print("--- Account type: " + user.get_emp_type())
        print("--- Store ID: " + str(user.get_emp_store_no()))
        print("\n")

        print(">>You are currently at Home Menu page")
        print("\n")
        print("--- Please enter the option (1-6)")
        print("1. Manage Inventory")
        print("2. Manage Orders")
        print("3. View Profile")
        print("4. Manage Staff Information")
        print("5. View Report")
        print("6. Logout")
        print("\n")

        x = 0
        while x == 0:
            option = input("--- Enter your option: ")

            if option == "1" or option == "3" or option == "4":
                print("!!! [ERROR] This function is currently NOT available !!!")
                print("!!! You will be directed to HOME MENU page  !!!")
                display_home_menu(user)
                x = 1
            elif option == "2":
                # manage_order()
                print("[Test] option 2 selected")
                x = 1
            elif option == "5":
                # view_report()
                print("[Test] option 5 selected")
                x = 1
            elif option == "6":
                logout(user)
                x = 1
            else:
                print("!!! [ERROR] Please enter a number between 1 and 6 !!!")

    elif user.get_emp_type() == "Manager":
        print("    ********** Welcome " + user.get_emp_name() + " **********    ")
        print("--- Account type: " + user.get_emp_type())
        print("--- Store ID: " + str(user.get_emp_store_no()))
        print("\n")

        print(">>You are currently at Home Menu page")
        print("\n")
        print("--- Please enter the option (1-5)")
        print("1. Manage Inventory")
        print("2. Manage Orders")
        print("3. View Profile")
        print("4. Manage Staff Information")
        print("5. Logout")
        print("\n")

        x = 0
        while x == 0:
            option = input("--- Enter your option: ")

            if option == "1" or option == "3" or option == "4":
                print("!!! [ERROR] This function is currently NOT available !!!")
                print("!!! You will be directed to HOME MENU page  !!!")
                display_home_menu(user)
                x = 1
            elif option == "2":
                # manage_order()
                print("[Test] option 2 selected")
                x = 1
            elif option == "5":
                logout(user)
                x = 1
            else:
                print("!!! [ERROR] Please enter a number between 1 and 5 !!!")

    else:
        print("    ********** Welcome " + user.get_emp_name() + " **********    ")
        print("--- Account type: " + user.get_emp_type())
        print("--- Store ID: " + str(user.get_emp_store_no()))
        print("\n")

        print(">>You are currently at Home Menu page")
        print("\n")
        print("--- Please enter the option (1-4)")
        print("1. Manage Inventory")
        print("2. Manage Orders")
        print("3. View Profile")
        print("4. Logout")
        print("\n")

        x = 0
        while x == 0:
            option = input("--- Enter your option: ")

            if option == "1" or option == "3":
                print("!!! [ERROR] This function is currently NOT available !!!")
                print("!!! You will be directed to HOME MENU page  !!!")
                display_home_menu(user)
                x = 1
            elif option == "2":
                # manage_order()
                print("[Test] option 2 selected")
                x = 1
            elif option == "4":
                logout(user)
                x = 1
            else:
                print("!!! [ERROR] Please enter a number between 1 and 4 !!!")


if __name__ == '__main__':
    user_list = load_user()
    current_user = login(user_list)
    if current_user.get_emp_type() == "Owner":
        select_store(current_user)
    display_home_menu(current_user)
