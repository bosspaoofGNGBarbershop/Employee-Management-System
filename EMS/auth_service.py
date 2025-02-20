class AuthService:
    def __init__(self, esb):
        self.esb = esb
        self.users = {"john_doe": "password123"}

    def handle_message(self, message):
        if "username" in message and "password" in message:
            self.authenticate(message["username"], message["password"])

    def authenticate(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"User {username} authenticated.")
        else:
            print(f"Authentication failed for user {username}.")
