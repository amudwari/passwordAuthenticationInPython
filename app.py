
def array():
    username = input("Please enter your Username: ")
    with open("password.txt") as password:
        lines = [line.split() for line in password]
        # print(lines)

        result = [list(i) for i in zip(*lines)]
        names = result[0]
        if username in names:
            print("Verified User!")
            check(username)
        else:
            print("No Username Found")

def md5(password):
    import hashlib
    result = hashlib.md5(password.encode())
    return result.hexdigest()

def check(username):
    password_file = open("password.txt", "r")
    for lines in password_file:
        line = lines.split()
        name = line[0]
        salt = line[1]
        hash = line[2]
        #print(name)
        if username == name:
            password = input("Please Enter your Password: ")
            combinedWord = salt + password
            newHash = md5(combinedWord)
            if newHash == hash:
                print("You are a verified user")
            else:
                print("Wrong password")
    password_file.close()
    exit()

def checkUser():
    username = input("enter Username: ")
    password_file = open("password.txt", "r")

    for lines in password_file:
        line = lines.split()
        name = line[0]
        #print(name)
        if username == name:
            goto = check(username)
            break
        else:
            print("try again")
    password_file.close()

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
        #checkUser()
        #file_read("password.txt")
        array()

def generateValues():
    import random
    randomNum = random.randrange(10, 100, 1)
    return randomNum

def credentials():
    name = input("Enter your name:")
    password = input("Enter your password:")

    randomNum = generateValues()
    password_file = open("password.txt", "a")

    combinedWord = str(randomNum) + password
    hashValue =  md5(combinedWord)
    password_file.write("\n" + name + "  " + str(randomNum) + "  " + hashValue)

    password_file.close()
    print("""Credentials successfully added!! """)

    userChoice = int(input("Enter '1' to go to menu OR 0 to EXIT: "))
    if userChoice == 1:
        menu()
    elif userChoice == 0:
        return
    else:
        print("invalid input")

menu()
generateValues()




