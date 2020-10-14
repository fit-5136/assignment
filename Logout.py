from display_home_menu import *


def logout(user):
    print(user.get_emp_name() + ", Do you want to log out?")
    print("Please enter 1 or 2 \n 1. Yes \n 2. No")

    x = 0
    while x == 0:
        option = input("Please enter your option: ")
        if option == "1":
            print("*** Log out successful ***")
            x = 1
        elif option == "2":
            display_home_menu(user)
            x = 1
        else:
            print("Please enter a number 1 or 2")