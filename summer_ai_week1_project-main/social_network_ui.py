from social_network_classes import SocialNetwork,Person

social_network = SocialNetwork()

def userLogin():
    boolean1 = True
    while boolean1:
        current_account = input("Do you currently have an account? (Y or N) ")
        if current_account.upper() == "Y":
            login_user = input("What is your name? ")
            login_age = int(input("What is your age? "))
            for object in social_network.list_of_people:
                if (object.name == login_user) and (object.age == login_age):
                    input("Correct Login!")
                    boolean1 = False
        elif (current_account.upper() == "Y") and (boolean1 == True):
            print("Incorrect Login!")
        elif current_account.upper() == "N":
            createAccount()
            break
        else:
            print("Invalid input!")

def createAccount():
    create = input("Would you like to create an account? (Y or N) ")
    if create.upper() == "Y":
        new_name = input("What is your name? ")
        new_age = input("What is your age? ")
        for object in social_network.list_of_people:
            if (object.name == new_name) and (object.age == new_age):
                print("Account was created successfully!")
                print(social_network.list_of_people)
                break
            else:
                print("Username already taken!")
    elif create.upper() == "N":
        userLogin()
    else:
        print("Invalid Input!")

def mainMenu():
    print("")
    print("########################################################")
    print("1. Manage my account")
    print("2. Log Out")
    print("########################################################")
    return int(input("Please Choose a number: "))

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. Send a message")
    print("5. View all my messages")
    print("6. <- Go back ")
    return int(input("Please Choose a number: "))
