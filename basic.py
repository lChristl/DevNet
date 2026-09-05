##############VARIABLES##############
print("#1 Variables")
my_name = "Christian"
my_age = 20
favorite_subject = "DevNet"
print(f"Hi, I'm {my_name}, I'm {my_age} years old, and I love {favorite_subject}.")

##############DATA TYPES##############
print("#2 Data Types")
a = 10
b = 10.5
c = "10"
d = True

print(int(a))
print(float(a))
print(str(a))
print(bool(a))


##############TYPE CONVERSION##############
# TODO: Fix the broken code below using type conversion
print("2b. Type Conversion")
a = 10
c = int("5")

# This breaks:
# result = a + c

# Fix it here:
result = a + c
print(result)

# BONUS: convert 3.9 into an int. What happens to the decimal part? 
f = int(3.9)
print(f)

##############PRINT, INPUT & STRING FORMATTING##############
print("3. Print, Input & String Formatting")

name = input("What's your name? ")
age = int(input("How old are you? ")) + 5  # this comes back as a STRING
hobby = input("What's your favorite hobby? ")

print(f"Hello I am {name}, my age is {age}, and my hobby is/are {hobby} ")





##############OPERATORS##############
print("4. Operators")
# TODO: Simple grade checker

score = 85
passing_score = 75

# 1. Check if the student passed (comparison operator)
passed = score > passing_score

# 2. Check if the score is even (modulo)
is_even = score % passing_score

# 3. Check if the student passed AND scored above 80 ('and')
honor_roll = score = passing_score and score > 80

print(passed, is_even, honor_roll)



##############CONTROL FLOW##############
print("5. Control Flow")
# TODO: Build a simple "bouncer" program

age = 18

# 1. if/elif/else:
#    "Welcome in!" if age >= 18
#    "Sorry, come back next year." if age is 17
#    "You're too young." otherwise
if age >= 18:
    countdown = [5,4,3,2,1,"Doors open!"]
    for x in countdown:
        print(x)
    print("Welcome in!")
elif age is 17:
    print("Sorry, come back next year.")
else:
    print("You're too young.")

# 2. BONUS: use a for loop to count down from 5 to 1, then print "Doors open!"

##############FINAL CHALLENGE##############
print("A.")
secret_number = 7
guess = int(input("Guess a number: "))

# TODO: if/elif/else — tell the user if their guess is too high, too low, or correct
if guess < 7:
    print("Too low")
if guess == 7:
    print("You guessed correctly")
if guess > 7:
    print("Too high")        


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
