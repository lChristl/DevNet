print("B.")

correct_username = "admin"
correct_password = "python123"

uname = input("Enter your username: ")
password = input("Enter your password: ")

if uname == correct_username and password == correct_password:
    print("Access granted")
else:
    print("Access denied")
# TODO: ask for username and password using input()
# TODO: check both using 'and'
# TODO: print "Access granted" or "Access denied"