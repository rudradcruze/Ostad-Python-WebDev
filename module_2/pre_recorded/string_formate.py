user_input = input("What is your name? ")

a = "Good Morning, {}. How are you?".format(user_input)

print(user_input)
print(a)


age = 25
f_name = "Francis"
l_name = "Rudra D Cruze"

text = "I am {f_name} {l_name}, {age} years old".format(f_name=f_name, l_name=l_name, age=age)
text2 = f"I am {f_name} {l_name}, {age} years old"

print(text)
print(text2)