class BankAccount:
    def __init__(self, accountNumber, balance):
        # ATTRIBUTES
        self.__accountNumber = accountNumber # - accountNumber (Private)
        self.__balance = balance # - balance (Private)
    # METHODS
    def set_account_number(self, accountNumber):
            self.__accountNumber = accountNumber
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("The balance must not be a negative number. Please enter a valid balance.")
    def get_account_number(self):
        return self.__accountNumber
    def get_balance(self):
        return self.__balance


# TEST RUN
if __name__ == "__main__":
    # Create the two bank account objects
    account1 = BankAccount(accountNumber=12345, balance=1000)

    print("Account 1")
    print(f"Account Number: {account1.get_account_number()}")
    print(f"Balance: ${account1.get_balance()}")


    print("\nUpdate balance to -100")

    account1.set_balance(-100)  # This will trigger the validation message
    print(f"Account Number: {account1.get_account_number()}")
    print(f"Balance: ${account1.get_balance()}")

