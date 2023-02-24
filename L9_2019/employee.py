class employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.' + last + '@company.com'
        employee.num_of_emps += 1 #class-value
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
        #raise_amount är specifik för valt emp


emp_1 = employee('Max', 'Mattsson', 50000)
emp_2 = employee('förnamn', 'efternamn', 40000)
print(emp_1.fullname())