username = raw_input("Please enter your username: ")
if username == "Maguire" or username =="Lindelof":
    print("Welcome back!" + username + ",Please enter your password!")
    password = raw_input("Password:")
    if username == "Maguire" and password == "Harry the slabhead":
        print("Logged in to Slabhead's PC")
    elif username == "Lindelof" and password == "Victor ice man":
        print("Logged in to Lindelof's PC")
    else:
        print("Incorrect password!")
        print("Access DENIED!")
else:
    print("NO such username! ")
    print("Acess denied")
