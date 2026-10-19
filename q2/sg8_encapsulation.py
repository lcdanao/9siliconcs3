class BankAccount:
    def __init__(self, accountNumber, balance):
        # ATTRIBUTES
        self.__accountNumber = accountNumber # - accountNumber (Private)
        self.__balance = balance # - balance (Private)
    # METHODS
    # Setter Methods
    def set_account_number(self, accountNumber):
            self.__accountNumber = accountNumber
    def set_balance(self, balance):
        if balance >= 0: # Ensures that the balance is not negative
            self.__balance = balance 
        else:
            print("The balance must not be a negative number.")  # Displays an error message
    # Getter Methods
    def get_account_number(self):
        return self.__accountNumber
    def get_balance(self):
        return self.__balance


# TEST RUN
if __name__ == "__main__":
    account1 = BankAccount(accountNumber=12345, balance=1000) # Creates the  bank account object

    print("Account 1")
    print(f"Account Number: {account1.get_account_number()}") # Displays the account number
    print(f"Balance: {account1.get_balance():.2f}") # Displays the balance formatted to two decimal places


    print("\nUpdate balance to -100")

    account1.set_balance(-100)  # Triggers the validation message
    print(f"Account Number: {account1.get_account_number()}") # Displays the account number
    print(f"Balance: {account1.get_balance():.2f}") # Displays the balance formatted to two decimal places