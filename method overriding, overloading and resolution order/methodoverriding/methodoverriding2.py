class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_pay(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus
    
    def calculate_pay(self):  
        return self.base_salary + self.bonus

class Salesperson(Employee):
    def __init__(self, name, base_salary, commission):
        super().__init__(name, base_salary)
        self.commission = commission
    
    def calculate_pay(self):  
        return self.base_salary + self.commission

# Usage
emp = Employee("John", 50000)
mgr = Manager("Alice", 60000, 10000)
sales = Salesperson("Bob", 45000, 8000)

print(f"{emp.name} pay: ${emp.calculate_pay()}")
print(f"{mgr.name} pay: ${mgr.calculate_pay()}")
print(f"{sales.name} pay: ${sales.calculate_pay()}")