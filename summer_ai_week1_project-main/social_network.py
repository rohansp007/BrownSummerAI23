from  social_network_classes import social_network,Person,all_friends_lists,FriendList
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
            manage_choice = social_network_ui.manageAccountMenu()
        else:
            continue
        if manage_choice == '7':
            continue
        else:
            if manage_choice == '1':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
                updated_userid = input("What would you like your new user ID to be? ")
                updated_age = int(input("What would you like your new age to be? "))
                updated_password = input("What would you like your new password to be? ")
                updated_user_found = False
                for person in social_network:
                    if (person.user_id == updated_userid):
                        print("This username is already in use!")
                        updated_user_found = True
                while not updated_user_found:
                    for index in range(len(social_network)):
                        if (social_network[index].user_id == current_userid):
                            social_network[index] = Person(updated_userid,updated_age,updated_password)
                            print("User info successfuly updated!") 
                            updated_user_found = True
                            break
                    if updated_user_found == False:
                        print("Couldn't update user credentials!")
                        updated_user_found = True
                        break
            if manage_choice == '2':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
                new_friend = input("What is the username of the friend you'd like to add? ")
                user_exist = True
                for person1 in social_network:
                    if (person1.user_id == current_userid) and (person1.password == current_password):
                        user_exist = False
                        current_object = person1
                        current_index = social_network.index(person1)
                if user_exist == True:
                    print("Something went wrong!")
                while not user_exist:
                    for person2 in social_network:
                        if (person2.user_id not in all_friends_lists[index].friendlist):
                            if (person2.user_id == new_friend):
                                all_friends_lists[current_index].add_friend(new_friend)
                    if user_exist == False:
                        print("Error! Make sure friend hasn't already been added or exists!")
                        user_exist = True
                        break
            if manage_choice == '3':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
                for person3 in social_network:
                    if (person3.user_id == current_userid):
                        for element in person3.friendlist:
                            print(element)
            if manage_choice == '4':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
                blocked_friend = input("What is the username of the user you'd like to block? ")
                done_blocked = True
                while done_blocked:
                    for person_class in social_network:
                        if (person_class.user_id == current_userid):
                            for friend1 in person_class.friendlist:
                                if blocked_friend == friend1:
                                    person_class.friendlist.remove(friend1)
                                    print("Friend removed successfully!")
                                    done_blocked = False
                    if done_blocked == True:
                        print("Incorrect credentials!")
            if manage_choice == '5':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
            if manage_choice == '6':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
    elif choice == '3':
        break