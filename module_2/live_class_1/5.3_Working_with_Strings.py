message = "Hello, Python!"

# Converting case
print(message.upper())      # Shows: HELLO, PYTHON!
print(message.lower())      # Shows: hello, python!

# Finding and counting
print(message.count('o'))   # Shows: 2
print(message.find('Python'))  # Shows: 7

# Removing whitespace
text = "   Hello   "
print(text.strip())        # Shows: Hello