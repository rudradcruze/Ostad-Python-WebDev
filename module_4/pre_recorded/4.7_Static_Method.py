class School:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def calculate_grade(marks):
        if marks >= 90:
            return "A+"
        else:
            return "F"

sc1 = School("Rudra", 10)
sc2 = School("Rohan", 11)

print(sc1.calculate_grade(95))
print(sc2.calculate_grade(80))

print(School.calculate_grade(85))