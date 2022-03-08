class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0


user_1 = User("001", "lenny")
print(user_1.followers)

