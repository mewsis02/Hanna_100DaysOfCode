# DAY 17 : Creating Classes

class User:

    def __init__(self, user_id, username):
        print("\nnew user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0  # can do this to set default values
        self.following = 0  # can do this to set default values

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "ZANE".title())
print(f"Hello {user_1.username}, You are user {user_1.id}.")

user_2 = User("002", "HANNA".title())
print(f"Hello {user_2.username}, You are user {user_2.id}.")

print("")
user_1.follow(user_2)
print(f"{user_1.username} now has {user_1.followers} followers, and {user_1.following} following.")
print(f"{user_2.username} now has {user_2.followers} followers, and {user_2.following} following.")
