class User:
    def __init__(self,id , name ):
        print("New user created")
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        user.following+=1


user1 = User(1, "Rituraj")  # 1st object -> constructor called
user2 = User(2, "Anusha")   # 2nd object -> constructor called
user3 = User(3, "Rakesh")   # 3rd object -> constructor called

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

