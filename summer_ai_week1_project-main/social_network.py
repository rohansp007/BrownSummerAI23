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
            manage_choice = social_network_ui.manageAccountMenu()
        else:
            continue
        if manage_choice == '8':
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
                        if (social_network[index].user_id == current_userid) and (social_network[index].password == current_password):
                            social_network[index] = Person(updated_userid,updated_age,updated_password,social_network[index].friendlist,social_network[index].receivedmessages,social_network[index].sentmessages)
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
                    print("Incorrect credentials!")
                while not user_exist:
                    for person2 in social_network:
                        if (person2.user_id not in current_object.friendlist):
                            if (person2.user_id == new_friend):
                                person1.add_friend(new_friend)
                                social_network[current_index] = person1
                                print("Friend added successfully!")
                                user_exist = True
                                break
                    if user_exist == False:
                        print("Error! Make sure friend hasn't already been added or exists!")
                        user_exist = True
                        break
            if manage_choice == '3':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
                found_object = False
                for person3 in social_network:
                    if (person3.user_id == current_userid) and (person3.password == current_password):
                        for element in person3.friendlist:
                            print(element)
                        found_object = True
                if found_object == False:
                    print("Couldn't find user!")
            if manage_choice == '4':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
                blocked_friend = input("What is the username of the user you'd like to block? ")
                found_blocked = False
                for index2 in social_network:
                    if (index2.user_id == current_userid) and (index2.password == current_password):
                        for friend in index2.friendlist:
                            if blocked_friend == friend:
                                index2.friendlist.remove(friend)
                                print("Friend Blocked!")
                                found_blocked = True
                        if found_blocked == False:
                            print("Couldn't find user or incorrect credentials!")
            if manage_choice == '5':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
                found_recipient = False
                for person1 in social_network:
                    if (person1.user_id == current_userid) and (person1.password == current_password):
                        sender = person1.user_id
                        sender_object = person1
                        message = input("What is the message you'd like to send? ")
                        recipient = input("What is the username of the recipient? ")
                        for person2 in social_network:
                            if (person2.user_id == recipient):
                                person2.send_message(f'{sender}: {message}')
                                person1.all_sent_messages(f'{sender}: {message}')
                                print("Message sent successfully!")
                                found_recipient = True
                if found_recipient == False:
                    print("Sorry! Could not send message!")
            if manage_choice == '6':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
                found_user = False
                for person3 in social_network:
                    if (person3.user_id == current_userid) and (person3.password == current_password):
                        found_user = True
                        for message in person3.receivedmessages:
                            print(message)
                if found_user == False:
                    print("Couldn't find user!")
            if manage_choice == '7':
                current_userid = input("What is your username? ")
                current_password = input("What is your password? ")
                found_user = False
                for person3 in social_network:
                    if (person3.user_id == current_userid) and (person3.password == current_password):
                        found_user = True
                        for message in person3.sentmessages:
                            print(message)
                if found_user == False:
                    print("Couldn't find user!")
    elif choice == '3':
        break