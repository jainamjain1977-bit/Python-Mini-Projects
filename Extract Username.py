email = input("enter your email:");
username = " ";
for i in email:
    if i == "@":
        break;
    username = username + i;
print("username:",username);
