# Read user input
MIN_USERNAME_LENGTH = 5
ACCEPTED_TLS = [".com", ".bg", ".org", ".net"]


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


# Logic

while True:
    email_address = input()
    if email_address == "End":
        break
    if "@" not in email_address:
        raise MustContainAtSymbolError("Email must contain @")

    user_name, domain = email_address.split("@")

    if len(user_name) < MIN_USERNAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    domain_name, tls = domain.split(".")
    if f".{tls}" not in ACCEPTED_TLS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    # Print output
    print("Email is valid")
