class Employee:
    """Define Employee class"""

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay_amount):
        """Initialize class"""

        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
        self.pay_amount = pay_amount

        Employee.num_of_emps += 1

    def apply_raise(self):
        self.pay_amount = int(self.pay_amount * self.raise_amt)

    @classmethod
    def change_rise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def get_attr_from_str_with_dash(cls, emp_str):
        """set class attr from single string with -"""

        f_name, l_name, amount = emp_str.split('-')
        return cls(f_name, l_name, amount)

    @staticmethod
    def is_work_day(day):
        """Return if the day is work day"""
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False

    def __str__(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}, pay: {self.pay_amount}"


emp_1 = Employee("Sayed", "Nuruddin", 5)
emp_2 = Employee("Zahid", "Hassan", 4)

# example string data with -
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

emp_3 = Employee.get_attr_from_str_with_dash(emp_str_1)

print(emp_2)
print(emp_3)

import datetime

my_date = datetime.date(2021, 10, 11)

print(Employee.is_work_day(my_date))
