ACTIVITY 3:
—-------------

Instruction:
Create a BankAccount class with attributes that can be accessed and updated through
methods.
Goal: Apply the concept of Encapsulation by designing a BankAccount class that protects its
data and controls access and modification.
Role: You are a junior software developer hired by a bank to create a secure bank account
system. Your task is to make sure sensitive information is properly protected.
Audience: Your work will be reviewed by your teacher (as the lead developer)
Situation: A bank wants to digitize its account management system. However, they are
concerned about security and data integrity.

They need a BankAccount class that:
Protects the account number:
Prevents negative balances
Allows controlled access through methods
You must design the class in accordance with proper encapsulation principles.

Product:
A Python code of the class BankAccount with the following requirements:
private attributes
account_number and balance
public setter methods
setter for account number
setter for balance
Note: the balance must not be negative; if it is, ignore it and issue a warning.

public getter methods using @property decorator
getter for account number
getter for balance

An object of the class BankAccount that utilizes all the public methods.
A formatted balance amount on the output display.
