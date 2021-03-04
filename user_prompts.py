"""
Displays a prompt for the user. Allows a user to login to his or her account,
or create a new account.

After successful login, a secret message is displayed.
"""
import account_creation

def display_prompt():
    user_input = input("Type \'login\' or \'create account\': ")
    if user_input == 'create account':
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")

if __name__ == "__main__":
    display_prompt()
