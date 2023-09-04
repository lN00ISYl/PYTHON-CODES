username = input("USERNAME:")
password = input("PASSWORD:")
username_right= "admin"
password_right= "1234"

if username == username_right and password == password_right:
    print("YOU HAVE ENTERED THE RIGHT USERANME AND PASSWORD")
elif not username == username_right and password == password_right:
    print("WRONG USERNAME")
elif not password == password_right and username == username_right:
    print("WRONG PASSWORD")
else:
    print("INCORRECT PASSWORD AND USERNAME")