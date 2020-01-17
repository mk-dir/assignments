username="Mark"
password=1234
email="mark@gmail.com"

uName=str(input("Enter Username: "))
if uName!=username:
    print("Invalid Email")

mail=str(input("Enter Email: "))
if mail!=email:
    print("Invalid Email")

passw=int(input("Enter Password: "))

if uName==username and mail==email and passw==password:
    print("Login Successful")
else:
    print("Check your credentials and try again")