
def md5(password):
    import hashlib
    result = hashlib.md5(password.encode())
    return result.hexdigest()

def check(userName):
    password_file = open("password.txt", "r")
    for lines in password_file:
        line = lines.split()
        name = line[0]
        salt = line[1]
        hash = line[2]
   # print(name)
        if userName == name:
            password = input("Please Enter your Password: ")
            combinedWord = salt + password
            newHash = md5(combinedWord)
            #print(newHash)
            if newHash == hash:
                print("You are a verified user")
    password_file.close()
    exit()

def checkUser():
    username = input("enter Username: ")
    password_file = open("password.txt", "r")

    for lines in password_file:
        line = lines.split()
        name = line[0]
        #print(name)
        if username != name:
            print("Unverified User!!!")
            exit()
        else:
            goto = check(username)
            goto()

def menu():
    print("""Welcome to Password Authentication Software

    Please Choose one of the following:
    1. Sign up to the system
    2. Login to the system
    3. Exit""")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        credentials()
    elif choice == 3:
        exit()
    elif choice == 2:
        checkUser()


def generateValues():
    import random
    randomNum = random.randrange(100, 999, 1)
    return randomNum



def credentials():

    name = input("Enter your name:")
    password = input("Enter your password:")

    randomNum = generateValues()
    password_file = open("password.txt", "a")

    combinedWord = str(randomNum) + password
    hashValue =  md5(combinedWord)
    password_file.write( "\n" + name + "  " + str(randomNum) + "  " + hashValue )

   # password_file.write( "\n" + name + hashValue)

    password_file.close()
    print("""Credentials successfully added!! """)

    userChoice = int(input("Enter '1' to go to menu OR 0 to EXIT: "))
    if userChoice == 1:
        menu()
    elif userChoice == 0:
        return
    else:
        print("invalid input")

    """def checkUser(name):
    #password = input("Please Enter Password: ")
    password_file = open("password.txt", "r")
    for line in password_file:
        lines = password_file.split()
        print(lines)
        return lines
    password_file.close()"""

menu()
generateValues()




