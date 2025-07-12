# Define the object
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first = first_name
        self.last = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_pay(self):
        return self.pay

    def bonus(self):
        return 0.10 * self.pay

# The derived manager class
class Manager(Employee):
    def __init__(self, first_name, last_name, pay):
        super().__init__(first_name, last_name, pay)

    def bonus(self):
        return 0.20 * self.pay

    def long_term_bonus(self):
        return 0.50 * self.pay

# Instantiate the object
employee_1 = Employee('Diego', 'Smith', 60000.00)
manager_1 = Manager('Jim', 'Smith', 90000.00)

# Use the object
print(employee_1.email)
print("First name:", employee_1.get_first())
print("Last name:", employee_1.get_last())
print("Annual salary:", employee_1.get_pay())
print("Bonus salary:", employee_1.bonus())

print() # Blank line for separation

print(manager_1.email)
print("First name:", manager_1.get_first())
print("Last name:", manager_1.get_last())
print("Annual salary:", manager_1.get_pay())
print("Bonus salary:", manager_1.bonus())
print("Long Term Bonus:", manager_1.long_term_bonus())