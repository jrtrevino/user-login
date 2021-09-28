# User Login
A small project to verify user login information. A user is presented an option to sign in or create an account.
User login information is stored in a file named db.json where passwords are hashed and salted using PyCrypto.

On sign in, if an invalid username or password is inputted, an error message is displayed. If a valid username and password is given, a message generated by the user on account creation is displayed!

On account creation, if a username is already taken, an error is thrown.

## Password/Account Requirements
A valid password follows these characteristics:
  - A minimum of 8 characters (1)
  - At least 1 uppercase and lowercase letter (2)
  - At least 1 numerical character (3)
  - At least 1 special character. < or > is not a valid special character. (4)

A valid account name follows these characteristics:
  - Longer than three characters (1)
  - Cannot contain <, >, or :. (2)

## Dependencies
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
To start the json-server, type:
```
json-server db.json
```

To run this program, type:

```
python3 src/ui/user_prompts.py
```
[json-server]: https://www.npmjs.com/package/json-server
