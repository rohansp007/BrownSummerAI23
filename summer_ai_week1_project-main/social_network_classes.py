social_network = []
all_friends_lists = []
class Person():
    def __init__(self,user_id,age,password):
        self.user_id = user_id
        self.age = age
        self.password = password

    def create_account(self,new_name,new_age,new_password):
        social_network.append(Person(new_name,new_age,new_password))

