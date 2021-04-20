class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def return_user(self):
        return (self.username, self.password)

    def __str__(self):
        return f"Username is {self.username}"
