"""
Determine if a password contains valid characters and follows
password requirements.

For this CLI program, a password must contain:

- A minimum of 8 characters (1)
- At least 1 uppercase and lowercase letter (2)
- At least 1 numerical character (3)
- At least 1 special character. < or > is not a valid special character. (4)
"""
import re

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
