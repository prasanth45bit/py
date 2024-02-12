def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Check if username and password match a predefined set of credentials
    if username == "admin" and password == "password":
        print("Login successful!")
    else:
        print("Incorrect username or password. Please try again.")

# Main function to execute the login program
if __name__ == "__main__":
    login()
