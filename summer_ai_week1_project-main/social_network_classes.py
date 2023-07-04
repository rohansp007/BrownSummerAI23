social_network = []

class Person():
    def __init__(self,user_id,age,password,friendlist,receivedmessages,sentmessages):
        self.age = age
        self.user_id = user_id
        self.password = password
        self.friendlist = friendlist
        self.receivedmessages = receivedmessages
        self.sentmessages = sentmessages

    def create_account(self,new_name,new_age,new_password,new_friendlist,new_received_messages,new_sent_messages):
        social_network.append(Person(new_name,new_age,new_password,[],[],[]))
    
    def add_friend(self,new_friend):
        self.friendlist.append(new_friend)
    
    def view_all_friends(self,username):
        for persona in social_network:
            if (persona.user_id == username):
                for friend in persona.friendlist:
                    print(friend)
    
    def block_friend(self,blocked_friend):
        self.friendlist.remove(blocked_friend)
        self.blockedlist.append(blocked_friend)
    
    def send_message(self,message):
        self.receivedmessages.append(message)
    
    def all_sent_messages(self,sent_message):
        self.sentmessages.append(sent_message)