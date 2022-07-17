# 22. Health Management System

# 3 users
def getdate():
    import datetime
    return datetime.datetime.now()


# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

import datetime

def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            value = input("Type here\n")
            with open("User1-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("User1-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            value = input("Type here\n")
            with open("User2-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("User2-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            value = input("Type here\n")
            with open("User3-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("User3.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("Please enter valid input (1(User1),2(USer2),3(User3)")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            with open("User1-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("User1-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            with open("User2-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("User2-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            with open("User3-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("User3-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter valid input (User1,User2,User3)")


print("------Health Management System------ ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for User1 2 for User2 3 for User3 "))
    take(b)
else:
    b = int(input("Press 1 for User1 2 for User2 3 for User3 "))
    retrieve(b)
