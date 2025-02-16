class School:
    # Class variable
    school_name = "ABC School"

    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

sc1 = School("Rudra", 10)
sc2 = School("Rohan", 11)

print(sc1.school_name)
print(sc1.name)
print(sc1.age)

sc1.school_name = "XYZ School"
School.school_name = "PQR School"

print(sc1.school_name)

print(sc2.school_name)
print(sc2.name)
print(sc2.age)

sc3 = School("Rahul", 12)
print(sc3.school_name)
