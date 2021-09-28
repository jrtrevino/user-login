# User Login
A small project to verify user login information. A user is presented an option to sign in or create an account.
User login information is stored in a file named usernames.txt where passwords are hashed and salted using PyCrypto.
On sign in, if an invalid username or password is inputted, then an error is thrown. If a valid username and password is given, a secret message is displayed!
On account creation, if a username is already taken, an error is thrown.
Will eventually change text file with hashed passwords to an sql-based database.

## dependencies
This module requires bcrypt for hashing and salting. To install, type:
```
$ python -m pip install bcrypt
```
A local json server with REST supported CRUD endpoints is used in this app. I used [json-server], an npm package. 
To install, type:
```
$ npm install json-server
```


## Running
python3 src/ui/user_prompts.py

[json-server]: https://www.npmjs.com/package/json-server
