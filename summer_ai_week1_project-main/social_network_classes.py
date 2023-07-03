social_network = []

class Person():
    def __init__(self,user_id,age,password,friendlist):
        self.user_id = user_id
        self.age = age
        self.password = password
        self.friendlist=[]

    def create_account(self,new_name,new_age,new_password,new_friendlist,new_blockedlist):
        social_network.append(Person(new_name,new_age,new_password,new_friendlist,new_blockedlist))
    
    def add_friend(self,new_friend):
        self.friendlist.append(new_friend)
    
    def view_all_friends(self,username):
        for persona in social_network:
            if (persona.user_id == username):
                for friend in persona.friendlist:
                    print(friend)
    
    def block_friend(self,blocked_friend):
        self.friendlist.remove(blocked_friend)