### This is a basic application that allows a user to register or login

# Prompt new credentials and store in a file
def prompt_credential_creation():
    print("Enter your username: ")
    username = input()
    print("Enter your password: ")
    password = input()

    with open("credentials.txt", "w") as file:
        file.write(f"{username},{password}")

    return username, password

# Prompt credentials and check if they match the stored credentials
def prompt_login():
    username = input("Username:")
    password = input("Password:")

    with open("credentials.txt", "r") as file:
        stored_username, stored_password = file.read().split(",")

    return username == stored_username and password == stored_password

def main():
    option = input("Register or Login? (R/L):")
    
    if option == "R":
        # Prompt the user to register credentials
        username, password = prompt_credential_creation()
        print(f"Username: {username}, Password: {password}")
    elif option == "L":
        # Prompt the user to login
        successful_login = prompt_login()
        if successful_login:
            print("Login successful")
        else:
            print("Login failed")

if __name__ == "__main__":
    main()


