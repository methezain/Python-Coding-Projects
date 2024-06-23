class User_Class:
    
    def __init__(self, id, username):  # constructor 
        self.id = id # attributes 
        self.username = username
        self.followers = 0
        self.age = 0
        self.address = ""
        
        
user = User_Class(4004, "Ali Zain")

print(user.username)  