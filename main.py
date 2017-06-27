
#Import variables from existing file.
from spy_details import spy, Spy, ChatMessage, friends
#Import class from file for encoding and decoding hidden messages.
from steganography.steganography import Steganography
from termcolor import *
import colorama

#Displays the list of existing status choices.
STATUS_MESSAGES = ["Some infinities are bigger than other infinities.", "For you, a thousand times over.", "Hakuna Matata!"]
colorama.init()
print "Hello! Welcome on board."

question = "Are you an existing user " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

#Function to add a new status to the list.
def add_status():
    updated_status_message = None

    if spy.current_status_message != None:
        print 'Your existing status message is %s \n' %(spy.current_status_message)
    else:
        print 'Oops! No status set. \n'

    default = raw_input("Wanna choose from existing statuses? ")

#Convert the input into upper case.
    if default.upper() == "N":
        new_status_message = raw_input("What describes your mood the best?")

#Check the length of status for no input.
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':
        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

#Selecting a status from existing list of statuses.
        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

#Function to add a new friend.
def add_friend():

    new_friend = Spy('','',0,0.0)
    new_friend.name = raw_input("Please add your friend's name: ")

#Handling edge case scenarios.
    if set('[~!@#$%^&*()_+{}":;\']+$ " "').intersection(new_friend.name):
        print "Invalid entry. "
        new_friend.name = raw_input("Please re enter a valid name")
    else:
        print new_friend.name

    new_friend.salutation = raw_input("How would you like to address them? ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = raw_input("How old is your friend?")
    new_friend.age = int(new_friend.age)
    new_friend.rating = raw_input("And their rating too please?")
    new_friend.rating = float(new_friend.rating)

#Mandatory conditions to be satisfied for adding a friend.
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print "Congratulations! You have a new friend."
    else:
        print "Uh huh! Your friend is not good enough. Try again with different details."

    return len(friends)

#Function to select a friend.
def select_a_friend():
    item_number = 0

    for friend in friends:
        print "%d. %s %s aged %d, with rating %.2f is online." %(item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1
    friend_choice = raw_input("Choose from your list of friends:")
    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#Function to send a secret message.
def send_message():
    friend_choice = select_a_friend()
    original_image = raw_input("Enter the file name. \n")
    output_path = "output.jpg"
    text = raw_input("Enter the message or choose one of these options for emergency situations : 1.SOS 2.SAVE ME 3.HELP ME. \n")
    print "Wait untill your secret message is encoded in the image!"
    Steganography.encode(original_image, output_path, text)
    new_chat = ChatMessage(text,True)
    friends[friend_choice].chats.append(new_chat)
    print "Your secret message has been encoded successfully."


#Function to read a secret message.
def read_message():
    sender = select_a_friend()
    output_image = raw_input("Kindly enter the file path.")
    secret_message = Steganography.decode(output_image)
    print 'The secret message is : ' + secret_message
    if secret_message.upper()=="SOS" or secret_message.upper()=="SAVE ME" or secret_message.upper()=="HELP ME":
        print "Gotcha! I'll get back to you ASAP!"



#Handles the cases when the message is blank.
    if len(secret_message) == 0:
        print "Trynna make a fool of me?"
    else:
        print "You are good to go."

    new_chat = ChatMessage(secret_message,False)
    friends[sender].chats.append(new_chat)
    words = secret_message.split()
    print 'Number of words in secret messages : ' + str(len(words))


#Function to read the chat history with chosen friend.
def read_chat_history():
    read_for = select_a_friend()
    print "\n"

    for chat in friends[read_for].chats:

        if chat.sent_by_me:
            cprint (chat.time.strftime("%d %B %Y"), 'blue')
            cprint ("You said:", 'red')
            print chat.message
        else:
            cprint (chat.time.strftime("%d %B %Y"), 'blue')
            cprint (friends[read_for].name, 'red')
            print chat.message


#Function to start the chat application.
def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name

#Condition that keeps a check on age of the new user.
    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + ", age: " \
              + str(spy.age) + " and rating " + str(spy.rating) + ". We are now a team."
        show_menu = True

        while show_menu:
            menu_choices = "What would you want to do next? \n 1. Add a status update \n 2. Add a new friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()

                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print "You have %d new friends. Yay!" %(number_of_friends)

                elif menu_choice == 3:
                    send_message()

                elif menu_choice == 4:
                    read_message()

                elif menu_choice == 5:
                    read_chat_history()

                else:
                    show_menu = False

    else:
        print "Your age is not suitable."

if existing.upper() == "Y":
    password= raw_input('enter your password!')
    if password =='admin':
        start_chat(spy)
    else:
        print 'password incorrect!'

else:
    spy = Spy('','',0,0.0)
    spy.name = raw_input("Welcome to spy chat. Please enter your name.")

    if set('[~!@#$%^&*()_+{}":;\']+$ " "').intersection(spy.name):
        print "Invalid entry. "
        spy.name = raw_input("Please re enter a valid name!")
    else:
        print spy.name

    if len(spy.name) > 0:
        spy.salutation = raw_input("How would you like us to address you?  ")
        spy.age = raw_input("How old are you?")
        spy.age = int(spy.age)
        spy.rating = raw_input("Let us know your rating.")
        spy.rating = float(spy.rating)
        start_chat(spy)
    else:
        print "Add a valid spy name please."
