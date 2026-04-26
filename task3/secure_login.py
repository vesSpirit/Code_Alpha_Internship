import hashlib

# Stored hashed password
stored_password = hashlib.sha256("1234".encode()).hexdigest()

username = input("Enter Username: ")
password = input("Enter Password: ")

entered_password = hashlib.sha256(password.encode()).hexdigest()

if username == "admin" and entered_password == stored_password:
    print("Login Successful")
else:
    print("Access Denied")