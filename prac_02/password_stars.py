password = input("Password: ")
PASSWORD_MIN_LENGTH = 0
while len(password) <= PASSWORD_MIN_LENGTH:
    password = input("Password: ")
print(len(password) * "*")
