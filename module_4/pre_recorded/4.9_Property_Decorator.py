class Employee:

    company_name = "ABC Limited"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    # @property
    # def get_salary(self):
    #     return self._salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary can not be negative")
        self._salary = value
 

emp = Employee("John", 50000)

print(emp.salary)
emp.salary = 60000

print(emp.salary)
# emp.salary = -10000
# print(emp.salary)


