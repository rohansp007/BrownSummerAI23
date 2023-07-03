social_network = []
social_network_friends = []

class Person():
    def __init__(self,user_id,age,password,friendlist=[],blockedlist=[]):
        self.age = age
        self.user_id = user_id
        self.password = password
        self.friendlist=[]
        self.blockedlist = []
    
    def create_account(self,new_name,new_age,new_password):
        social_network.append(Person(new_name,new_age,new_password))

class Friends():
    def __init__(self,friendlist,blockedlist):
        self.friendlist = []
        self.blockedlist = []