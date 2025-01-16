li = [(1, 'One'), (2, 'Two'), (3, 'Three')]

dt = {k:v for k, v in li}

print(dt)

s = 'asjvkjanskvrhrhgkjakjskfascasg'

unique_letters = {c for c in s}

print(unique_letters)

print(type(unique_letters))

color_choices = [('Messi', 'Blue'), ('Ronaldo', 'Red'), ('Neymar', 'Yellow'), ('Mbappe', 'Green'), ('Hazard', 'Black'), ('Kane', 'White'), ('Salah', 'Blue')]

print(color_choices)

color_dt = {name:color for name, color in color_choices}

color_set = {color for color in dt.values()}

color_set = {color for color in color_dt.values()}

print(color_dt)
print(color_set)