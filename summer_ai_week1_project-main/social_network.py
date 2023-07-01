from  social_network_classes import SocialNetwork,Person
import social_network_ui

ai_social_network = SocialNetwork()

if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    logging_in = social_network_ui.userLogin()
    choice = social_network_ui.mainMenu()