def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("Password: ")
    PASSWORD_MIN_LENGTH = 0
    while len(password) <= PASSWORD_MIN_LENGTH:
        password = input("Password: ")
    return password


def print_asterisks(password):
    print(len(password) * "*")


main()
