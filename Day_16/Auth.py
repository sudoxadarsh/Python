

users = {
    "adarsh" :"admin1234",
    "ved" : "professor1234"
    }

attempts = 3

while attempts > 0:

    userId = input("Enter user's ID: ")
    password = input("Password: ")

    if userId in users and users[userId] == password:
        print("user found n authenticated")
        
        break
    else:
        attempts -= 1
        print("invalid credentials")
        print(f"attempts remain: {attempts}")
        print("try again...!")
        

  