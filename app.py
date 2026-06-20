password = input("Enter password: ")

has_digit = any(char.isdigit() for char in password)
has_special = any(char in "@#$%&*" for char in password)
has_upper = any(char.isupper() for char in password)

if len(password) < 6:
    print("Weak Password")
elif has_digit and has_special and has_upper:
    print("Strong Password")
else:
    print("Medium Password")