users = {}

def check_or_add_user(username, password):
    if username in users:
        return users[username] == password
    else:
        users[username] = password
        return True
    
username = input("Enter username: ")
password = input("Enter password: ")

result = check_or_add_user(username, password)

if result:
    print("Access granted or new user registered.")
else:
    print("Incorrect password.")