class Employee:
    company_name = "ABC Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Employee Name: {self.name} - Salary: {self.salary}")
    
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

emp1 = Employee("Rudra", 10000)
emp2 = Employee("Rohan", 20000)

emp1.display_info()
emp2.display_info()

print(emp1.company_name)
print(emp2.company_name)

Employee.change_company_name("XYZ Company")

print(emp1.company_name)
print(emp2.company_name)
