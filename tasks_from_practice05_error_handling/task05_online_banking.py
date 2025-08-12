# Read user input
NEEDED_AGE = 18
class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin_code, balance, age = [int(x) for x in input().split(", ")]

# Logic
while True:
    user_input = input().split("#")
    command = user_input[0]
    if command == "End":
        break

    if command == "Send Money":
        money = int(user_input[1])
        pin = int(user_input[2])
        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin != pin_code:
            raise PINCodeError("Invalid PIN code")
        if age < NEEDED_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    if command == "Receive Money":
        received_money = int(user_input[1])
        balance += received_money / 2
        if received_money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        print(f"{received_money / 2:.2f} money went straight into the bank account")

