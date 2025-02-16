class Employee:
    company_name = "ABC Company"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name} - Salary: {self._salary}")


    def get_salary(self):
        return self._salary
    
    def set_salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            print("Invalid Salary")

emp1 = Employee("Rudra", 10000)
emp2 = Employee("Rohan", 20000)

emp1.display_info()
emp2.display_info()

print(emp1.get_salary())
print(emp2.get_salary())
