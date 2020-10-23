banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
user1='carolina'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

if user1 in banned_users:
    print("user is availible in banned_users")