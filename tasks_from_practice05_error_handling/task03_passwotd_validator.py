# Read user input
PASS_NUN_LENGTH = 8
SYMBOLS = ["@", "*", "&", "%"]


class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass

# Logic


while True:
    password = input()
    if password == "Done":
        break

    if len(password) < PASS_NUN_LENGTH:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password.isdigit() or password.isalpha() or all(not c.isalnum() for c in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(char in SYMBOLS for char in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
# Print output
    print("Password is valid")