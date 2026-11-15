class Patient: # Create the parent class Patient
    def __init__(self, name, bill_amount): # Initializes the attributes of the Patient class
        # ATTRIBUTES
        self.__name = name # - name (Private)
        self.__bill_amount = bill_amount # - bill_amount (Private)
    # METHODS
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0: # Ensures that the bill amount is not negative
            self.__bill_amount = bill_amount
        else:
            print("The bill amount must not be a negative number.")  # Displays an error message
    def calculate_bill(self):
        return self.__bill_amount
    def display_patient_type(self):
        return "Regular Patient"

class Senior(Patient): # Create the child class Senior (that inherits from Patient)
    def __init__(self, name, bill_amount): # Initializes the attributes of the Senior class
        # ATTRIBUTES
        super().__init__(name, bill_amount) # Calls the constructor of the parent class Patient to initialize name and bill_amount
    # METHODS
    def calculate_bill(self):
        discount = 0.2 * Patient.get_bill_amount(self) # 20% discount for senior citizens
        final_bill = Patient.get_bill_amount(self) - discount
        return final_bill
    def display_patient_type(self):
        return "Senior Citizen"

class PhilHealth(Patient): # Create the child class PhilHealth (that inherits from Patient)
    def __init__(self, name, bill_amount): # Initializes the attributes of the PhilHealth class
        # ATTRIBUTES
        super().__init__(name, bill_amount) # Calls the constructor of the parent class Patient to initialize name and bill_amount
    # METHODS
    def calculate_bill(self):
        discount = 0.15 * Patient.get_bill_amount(self) # 15% discount for PhilHealth members
        final_bill = Patient.get_bill_amount(self) - discount
        return final_bill
    def display_patient_type(self):
        return "PhilHealth Member"


# Creating Objects
patient1 = Patient("Juan Dela Cruz", 15000)
senior1 = Senior("Maria Santos", 15000)
philhealth1 = PhilHealth("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-----")
print(f"Patient Name: {patient1.get_name()}")
print(f"Patient Type: {patient1.display_patient_type()}")
print(f"Original Bill: ₱{patient1.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{patient1.calculate_bill():,.2f}")

print()
print(f"Patient Name: {senior1.get_name()}")
print(f"Patient Type: {senior1.display_patient_type()}")
print(f"Original Bill: ₱{senior1.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{senior1.calculate_bill():,.2f}")

print()
print(f"Patient Name: {philhealth1.get_name()}")
print(f"Patient Type: {philhealth1.display_patient_type()}")
print(f"Original Bill: ₱{philhealth1.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{philhealth1.calculate_bill():,.2f}")
