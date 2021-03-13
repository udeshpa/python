
class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + '.' + last + '@email.com'
        Employee.num_of_employees += 1

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __str__(self): #calling str will default to repr if not present
        return f'{self.fullname} {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prg_lang):
        super().__init__(first, last, pay)
        self.prg_lang = prg_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None): #Never pass a mutable type such as [] as default argument
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp  in self.employees:
            self.employees.remove (emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)


dev_1 = Developer('Uday', 'Deshpande', 100000, 'Java')
dev_2 = Employee('Test', 'User', 80000)

print(dev_1.__dict__)

print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(dev_1, Manager))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))

print(repr(dev_1))
print(str(mgr_1))

print(int.__add__(25, 34))
print(str.__add__('25', '34'))

print(dev_1 + dev_2)

print(len('test'))
print('test'.__len__())

print(len(dev_1))

dev_1.fullname = 'John Doe'
print(repr(dev_1))

del dev_1.fullname
print(repr(dev_1))

