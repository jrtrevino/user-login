"""
Determine if a password or username contains valid characters and follows
password requirements. Also can check if a username is already in the database.

For this CLI program, a password must contain:

- A minimum of 8 characters (1)
- At least 1 uppercase and lowercase letter (2)
- At least 1 numerical character (3)
- At least 1 special character. < or > is not a valid special character. (4)

a username must be:
- Longer than three characters (1)
- cannot contain <, >, or :. (2)
"""
import re
import bcrypt

# Returns true if password meets all requirements listed above. False if not.
def check_valid_password(password):
    if len(password) < 8:
        return False
    # search for password requirements
    req2lower = re.search('[a-z]', password)
    req2upper = re.search('[A-Z]', password)
    req3 = re.search('[0-9]', password)
    req4 = re.search('[^A-Za-z0-9<>]', password)
    if req2lower == None or req2upper == None or req3 == None or req4 == None:
        return False
    return True


# takes a binary string password (utf-8), applies salt then hashes using bcrypt
def gen_secure_password(password):
    salt = bcrypt.gensalt(rounds=12)
    hashed_pw = bcrypt.hashpw(password, salt)
    return hashed_pw


"""
Determines if a username can be used for an account. Checks if the username
follows the requirements and is not already in the database.
"""
def check_valid_username(username):
    username = username.rstrip()
    if len(username) < 4:
        return False
    req2 = re.search('[<>:]', username)
    if req2 == None and not check_if_username_exists(username):
        return True
    return False


"""
Determines if username is already in database. Returns true if username is
in the database, else false.
"""
def check_if_username_exists(username):
    account_file = open('./accounts/accounts.txt', 'r')
    users = account_file.readlines()
    for line in users:
        if username.lower().rstrip() in line.split(":")[0]:
            return True
    return False


def create_account(username, password):
    if check_valid_username(username) and check_valid_password(password):
        print("Valid username and password. Creating account!")
        password = gen_secure_password(password.encode('utf-8'))
        account_file = open('./accounts/accounts.txt', 'a+')
        account_file.write("{" + username + ":" + password.decode('utf-8') + "}")
        return True
    else:
        print("Invalid username and password. Try again")

    return False
