social_network = []
all_friends_lists = []
class Person():
    def __init__(self,user_id,age,password):
        self.user_id = user_id
        self.age = age
        self.password = password

    def create_account(self,new_name,new_age,new_password):
        social_network.append(Person(new_name,new_age,new_password))
    
class FriendList():
    def __init__(self,friendlist):
        self.friendlist = friendlist  

    def add_friend(self,new_friend):
        self.friendlist.append(new_friend)
    
    def view_all_friends(self,username):
        for persona in social_network:
            if (persona.user_id == username):
                for friend in persona.friendlist:
                    print(friend)
