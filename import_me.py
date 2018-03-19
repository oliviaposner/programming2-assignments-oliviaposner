def information(name, login):
    name = input("Enter your username:")
    if name == "Olivia Posner":
        login = input("Enter your password:")
        if login == "Hello":
            print("Welcome")
        else:
            print("Incorrect")
            done = True
    else:
        print("Access Denied")
        done = True