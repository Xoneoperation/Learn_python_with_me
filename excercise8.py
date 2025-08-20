usernames = ["Maxwell", "rahcel", "adeola", "admin", "joy", "titilayo"]

for username in usernames:
    if username == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()} thank you for logging in today. ")

usernamess = []
if usernames:
    for username in usernamess:
        print(f"Hello {username.title()} thank you for logging in today. ")
    else:
        print("We need to find some users !")

current_users = ["Maxwell", "rahcel", "adeola", "admin", "joy", "titilayo"]
new_users = ["james","Jackson", "Maxwell", "rahcel", "Adeola", "admin"]
# current_user_lower = current_users.lower() 
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"sorry, {new_user.title()} is already taken, please choose another usernanme.")
    else:
        print(f"welcome {new_user.title()}, we are happy to have you on board.")