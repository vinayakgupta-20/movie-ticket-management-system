from storage import load_data, save_data
from utils import is_valid_name
from logger import log_action

USER_FILE = "users.json"

def register_user():
    users = load_data(USER_FILE)
    username = input("Choose a username: ").strip()

    if not is_valid_name(username):
        print("Username cannot be empty. Try again.")
        return None
    
    for user in users:
        if user["username"].lower() == username.lower():
            print("This username is already taken. Please try another one.")
            return None
    password = input("Choose a password: ").strip()

    if not is_valid_name(password):
        print("Password cannot be empty.")
        return None

    new_user = {
        "username": username,
        "password": password
    }

    users.append(new_user)
    save_data(USER_FILE, users)
    log_action(f"New user registered: {username}")

    print(f"Account created successfully. Welcome {username}!")
    return username

def login_user():
    users = load_data(USER_FILE)
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for user in users:
        if user["username"].lower() == username.lower() and user["password"] == password:
            log_action(f"User logged in: {username}")
            print(f"Login successful. Welcome back {username}!")
            return username

    print("Invalid username or password.")
    log_action(f"Failed login attempt for username: {username}")
    return None