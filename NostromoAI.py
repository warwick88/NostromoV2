
# Hello User
# Lets build an AI

import time
from datetime import datetime



def active_user():
    global user1
    user1 = input("What is your name, user?: ")
    if user1 == "Dom":
        print("Welcome back Dom, always a pleasure to see you.")
    elif user1 == "Boo":
        print("Welcome back Boo!")
    else:
        print("Welcome new user, we are watching you")


def action():
    x = input("What would you like me to do " + user1 + "?: ")
    if x == "Weather":
        print("Sure lets check the weather in Kalamazoo for you")
        time.sleep(2)
        print("Collating, give me a moment...")
        time.sleep(3)
        print("Ok let's see weather")
    elif x == "Time":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
    elif x == "Nothing":
        print("Guess ill go fuck myself then, bye bye!")
        quit()
    else:
        print("I have no clue what your talking about, bye bye")
        quit()

    #print("What would you like me to do " + user1 + "?")


# def sentience():
#     y = "Well"
#     x = "fuck you"
#     r1 = input("What is your name user?")
#     print(y, x, r1)


#active_user()
#action()

#print(user1)
# sentience()
