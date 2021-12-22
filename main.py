import re
from accounts import Accounts, LowBalance


class InvalidCard(Exception):
    def __init__(self):
        print("Not a valid CARD!!")


def other_menu():
    mention = int(input("1. PIN change\n2.Block card"))
    card = input("Enter card number:")
    acc = Accounts.get_account_from_card(card)
    print(acc)

    if acc:
        mobile = input("Enter mobile:")
        pin = input("Enter old pin:")
        isvalid = acc.validate_phone_otp(mobile, pin)
        if isvalid and mention == 1:
            new_pin = input("Enter new pin:")
            acc.update_pin(new_pin)
            print("New pin set!!")
        elif isvalid and mention == 2:
            acc.block_card()
            print("Hurray! Card blocked successfully!!")


def withdrawal():
    mention = input("a. Enter the amount to withdrawal in terms of 200 RS\n"
                    "b. Check balance info\n"
                    "c. If balance low then display Error message (Low balance)\n"
                    "d. Exit\n"
                    "e. Thank you\n")

    if mention == "a":
        acc_num = input("Enter account number")
        acc = Accounts(acc_num)
        amt = int(input("Enter Amount for withdrawal:"))
        acc.withdraw(amt)
        print(f"Record updated successfully!! Current balance {acc.get_balance()}")


try:


    while True:
        print("Menu:")
        print("1. Withdrawal")
        print("2. Savings")
        print("3. Current")
        print("4. other")
        option = int(input("Please select transaction:\n"))
        if option > 4:
            raise ValueError
        elif option == 1:
            withdrawal()
        elif option == 4:
            other_menu()

except LowBalance as err:
    print(err)
except InvalidCard:
    pass
except ValueError:
    print("Please enter correct option")
except Exception as err:
    print(err)
finally:
    print("Thank you for using the service")




