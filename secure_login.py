import hashlib

username = input("Username: ")
password = input("Password: ")

stored_username = "admin"
stored_password_hash = hashlib.sha256("admin123".encode()).hexdigest()

entered_hash = hashlib.sha256(password.encode()).hexdigest()

if username == stored_username and entered_hash == stored_password_hash:
    print("Login Successful")
else:
    print("Login Failed")