
#AGE = int(input("ENTER YOUR AGE"))
 
#if AGE >= 18:
 #   print("YOU ARE GAE")

CREATE = input("INPUT A GMAIL:")
PASS = input (" SET A PASSWORD:")

username = CREATE
real_pass = PASS

USER = input("YOUR EMAIL:")
PASSWORD = input("ENTER YOUR PASS:")

email = username
Right_pass = real_pass

if USER == email and PASSWORD == Right_pass:
    print("you entered you right password and email")
elif not USER == email and PASSWORD == Right_pass:
    print("you Entered your email wrong")
elif USER == email and PASSWORD != Right_pass:
     print("you Entered the wrong password")
else:
    print("YOU ENTERED BOTH PASS AND EMAIL WRONG")

