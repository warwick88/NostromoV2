# This will be Nostromos Main file. Importing other dependencies
# Things to do
# Front end UI Tkinter or PySimpleGUI (which is a wrapper for Tkinter)
# Pickle for storing user profiles & information.
# import NostromoAI


import random
import NostromoAI as nos
import pickle
import UserDatabase as UD
import AILanguage as AI



# Great global variable info https://www.geeksforgeeks.org/global-local-variables-python/
# Love this guide! https://stackoverflow.com/questions/20061307/python-3-login-program-using-dictionaries


def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in UD.user_library2 and UD.user_library2[username] == password:
        print("Login successful!")
        global active_user
        active_user = username
        return
    else:
        print("User doesn't exist or wrong password!")
        exit()


def action():
    x = str(input("So "  + active_user + " "+ "What are we doing today?"))


login()

print(active_user + " " + random.choice(AI.greetings))

action()

# This example here works at least matching username, not yet pass.
# def login():
#    username = input("Username: ")
#    password = input("Password: ")
#    if username in UD.user_library2:
#        print("welcome")
#        print(UD.user_library2)
#    else:
#        print("Damn it")

# if username in UD.user_library2 and UD.user_library2[password] == password:
#    print("wow we logged in")
# else:
#    print("failure")

# print(UD.user_library2)
# def login():
#    login_username = input("Username: ")
#    username_password = input("Password: ")
#    print("we are testing")
#    if username_password.get(login_username) == login_password:
#        print("wow")
#        pass
#    else:
#        print("shit")
#        # Incorrect username/password match
#        pass


# login()
# logintwo()

# print(UD.user_library2)
# class Human:

# attr1 = "Human"
# attr2 = "Sex"

# def description(self):
# print("I am a",self.attr1)
# print("I am a",self.attr2)


# Warwick = Human()

# print(Warwick.attr1)
# Warwick.description()

# print(random.choice(AI.greetings))
# nos.active_user()
# nos.action()


# print(AI.greetings[0])
# print(AI.greetings[2])
