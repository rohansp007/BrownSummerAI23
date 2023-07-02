from  social_network_classes import social_network,Person
import social_network_ui

if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
while True:
    choice = social_network_ui.mainMenu()
    if choice == '1':
        social_network_ui.createAccount()
    elif choice == '2':
        login_bool = social_network_ui.userLogin()
        if login_bool == True:
            social_network_ui.manageAccountMenu()
        else:
            continue
        manage_choice = social_network_ui.manageAccountMenu()
        if manage_choice == '6':
            continue
        else:
            if manage_choice == '1':
                pass
            if manage_choice == '2':
                pass
            if manage_choice == '3':
                pass
            if manage_choice == '4':
                pass
            if manage_choice == '5':
                pass
    elif choice == '3':
        break