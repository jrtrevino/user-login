"""
Displays a prompt for the user. Allows a user to login to his or her account,
or create a new account.

After successful login, a secret message is displayed.
"""
import account_creation
import sys
import requests

db_url = "http://localhost:3000/"


def login(username, password):
    # salt password
    password = account_creation.gen_secure_password(password.encode('utf-8'))
    res = requests.get(db_url + "accounts/{}".format(username))
    print(res)
    if res.status_code == 200:
        print(res.json()['password'])
        return True
    else:
        print("Wrong username or password.")


def display_prompt():
    display = 1
    while (display):
        user_input = input("Type \'login\' or \'create account\': ")
        if user_input == 'login':
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if login(username, password):
                print("Exiting. Have a good day!")
                sys.exit(0)

        elif user_input == 'create account':
            display = "Welcome to account creation!\n"\
                "Usernames must contain at least four characters and not include "\
                "characters: < >\n\n"\
                "Passwords must be at least 8 characters and contain at least:\n"\
                "1 lower and 1 uppercase character,\n"\
                "1 Number,\n"\
                "1 special character (excluding < or >)\n"
            print(display)
            username = input("Please enter a username: ")
            password = input("Please enter a password: ")
            account_creation.create_account(username, password)

        else:
            print("Invalid input. Try again.")
            continue


if __name__ == "__main__":
    display_prompt()
