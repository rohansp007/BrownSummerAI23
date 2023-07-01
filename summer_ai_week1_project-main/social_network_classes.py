# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = []
    
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

class Person():
    def __init__(self,name,user_id,password,age,friendlist=[],blockedlist=[]):
        self.name = name
        self.age = age
        self.user_id = user_id
        self.password = password
        self.friendlist=[]
        self.blockedlist = []
    
    def create_account(self,new_name,new_age):
        self.list_of_people.append(Person(new_name,new_age))
    
    def update_details(self,old_name,old_age,new_name,new_age):
        found_user = False
        for object in self.list_of_people:
            if (object.name == old_name):
                self.list_of_people.remove(object)
                self.list_of_people.append(Person(new_name,new_age))
                found_user = True
                break
            if found_user == False:
                print("Sorry. You couldn't update your details since you didn't provide the correct information!")
            else:
                print("Details updated!")


    def add_friend(self,new_friend_name,new_friend_age):
        found_friend = False
        for friend2 in self.list_of_people:
            if (friend2.name == new_friend_name):
                self.friendlist.append(friend2)
                found_friend = True
                break
        if found_friend == False:
            print("Friend not found!")
        else:
            print("Friend successfully added!")

    def block_friend(self,blocked_friend_name,blocked_friend_age):
        found_blocked = False
        for friend1 in self.friendlist:
            if (friend1.name == blocked_friend_name):
                self.friendlist.remove(friend1)
                self.blockedlist.append(friend1)
                found_blocked = True
                break
        if found_blocked == False:
            print("You don't have them added as a friend!")
        else:
            print("User has been blocked!")

    def view_friends(self):
        for friend in self.friendlist:
            print(friend.name)

class Message(Person):
    def __init__(self,received_messages,sent_messages):
        SocialNetwork.__init__(self)
        Person.__init__(self)
        self.received_messages = []
        self.sent_messages = []