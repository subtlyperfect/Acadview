#Datetime is used to access current date and time of the system.
from datetime import datetime

class Spy:

#Self keyword is used to store the values in the constructor.
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#For storing, updating and deleting the chats.
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Miles Halter', 'Ms.', 24, 4.0)

friend_one = Spy('Alaska Young', 'Mr.', 27, 4.9)
friend_two = Spy('Takumi Hikohito', 'Ms.', 29, 4.2)
friend_three = Spy('Lara Buterskaya', 'Dr.', 25, 4.7)


#List of friends.
friends = [friend_one, friend_two, friend_three]

