def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
       if username == "admin" and password == "password":
        print("Login successful!")
    else:
        print("Incorrect username or password. Please try again.")
if __name__ == "__main__":
    login()
