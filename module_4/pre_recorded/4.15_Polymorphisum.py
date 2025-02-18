# 1. Method Overrriding
class GrandFather:
    def greet(self):
        print("GrandFather says")

class Father(GrandFather):
    def greet(self):
        print("Father says")

class Children(Father):
    def greet(self):
        print("Children says")

gf = GrandFather()
ff = Father()
cc = Children()

gf.greet()
ff.greet()
cc.greet()

# 2. Method OVerloading (doesn't support)

# class Person:

#     def area():
#         return 10


#     def area(a, b):
#         return a*b

# person = Person()

# print(person.area())
