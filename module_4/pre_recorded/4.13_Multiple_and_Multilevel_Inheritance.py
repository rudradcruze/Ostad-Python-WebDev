# class GrandFather:
#     def __init__(self, color, first_name):
#         self.color = color
#         self.first_name = first_name
    
#     def gf_method(self):
#         print("GrandFather method")

# class Father(GrandFather):
#     def __init__(self, last_name):
#         self.last_name = last_name
    
#     def father_method(self):
#         print("Father method")
    
# class Son(Father, GrandFather):
#     def __init__(self, color, first_name, last_name, age):
#         Father.__init__(self, last_name)
#         GrandFather.__init__(self, color, first_name)
#         self.age = age
    
#     def son_method(self):
#         print("Son method")

# son1 = Son("Brown", "John", "Doe", 25)
# son1.gf_method()
# son1.father_method()
# son1.son_method()


# Multiple Inheritance
