import datetime


class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
        Employee.num_of_employees += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        return True


emp_1 = Employee('Uday', 'Deshpande', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(emp_1)
print(emp_1.__dict__)
print(Employee.__dict__)

emp_1.raise_amount = 1.05
print(emp_1.__dict__)
print(Employee.__dict__)
print(emp_1.fullname())
print(Employee.num_of_employees)

Employee.set_raise_amount(1.06)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.pay)


emp_3_str = 'John-Doe-70000'
emp_4_str = 'Steve-Smith-30000'

emp_3 = Employee.from_string(emp_3_str)
emp_4 = Employee.from_string(emp_4_str)

print(emp_3.__dict__)
print(emp_4.__dict__)

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

#emp_1.first = 'Uday'
#emp_1.last = 'Deshpande'
#emp_1.email = 'udaydeshpande@test1.com'
#emp_1.pay = 50000

#emp_2.first = 'Test'
#emp_2.last = 'User'
#emp_2.email = 'test_user@test1.com'
#emp_2.pay = 60000

