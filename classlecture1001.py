# Conditionals and Recursion in Python

# Example: Converting minutes to hours and minutes
minutes = 145
hours = minutes // 60
remainder = minutes % 60
print(f'{hours} hours and {remainder} minutes')
# Alternatively
minutes = 145
hours, minutes = divmod(minutes, 60)  # Built-in Function, so faster!
print(f'{hours} hours and {remainder} minutes')

# Clock arithmetic example:
start_time = 11  # Start time is 11 AM
duration = 3     # Duration is 3 hours
end_time = (start_time + duration) % 12
print(f'End time: {end_time} PM')

# Checking multiple conditions using logical operators
x = 7
print(x > 0 and x < 10)  # True
print(x % 2 == 0 or x % 3 == 0)  # False

# Consider the somewhat complex boolean logic below
def complex_logic(a, b, c):
    if not (a or b) and not c:
        return True
    else:
        return False

# Example use
result = complex_logic(True, False, False)
print("Result:", result)

# Simplified logic using DeMorgan's law
def simplified_logic(a, b, c):
    if (not a and not b) and not c:
        return True
    else:
        return False

# Example use
result = simplified_logic(True, False, False)
print("Result after applying DeMorgan's law:", result)

x = 5
if x % 2 == 0:
    print(f'{x} is even')
else:
    print(f'{x} is odd')

# Chained conditional with elif
if x < 0:
    print('x is negative')
elif x == 0:
    print('x is zero')
else:
    print('x is positive')

# Nested conditionals
x = 7
if x > 0:
    if x < 10:
        print('x is a positive single-digit number')

# Simplified using and operator
if x > 0 and x < 10:
    print('x is a positive single-digit number')

# Simplified even farther with Pythonic syntax
if 0 < x < 10:
    print('x is a positive single-digit number')

# Recursive countdown function
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(5)

# Recursive function to print a string multiple times
def print_n_times(string, n):
    if n > 0:
        print(string)
        print_n_times(string, n-1)

print_n_times('Hello', 3)

# Stack diagram and recursion debugging
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)  # Stack diagram shows how values change

# Prompting for user input
name = input('What is your name? ')
print(f'Hello, {name}!')

# Handling integer input
while True:
    try:
        age = int(input('How old are you? '))
        print(f'{name}, you are {age} years old.')
        break
    except ValueError as ve:
        print("That's not a valid age. Please enter an integer!")

while True:
    try:
        height = float(input('How tall are you? '))
        print(f'{name} you are {height} feet tall.')
        break
    except ValueError as ve:
        print("That's not a valid height. Please enter float!")

# String stuff

a = "hello world"
print(f'len:{len(a)} Char: {a[1]}')

# Introduction to Return Values

import math

def circle_area(radius):
    area = math.pi * radius ** 2
    return area

# Using return value
radius = math.sqrt(42 / math.pi)
area = circle_area(radius)

# Display result
print(f"Area of circle: {area}")

def repeat(word, n):
    print(word * n)

result = repeat('Python, ', 3)
print(f"The return value is: {result}")

def repeat_string(word, n):
    return word * n

line = repeat_string('Python, ', 3)
print(f"Repeated string: {line}")

def absolute_value(x):
    if x < 0:
        return -x
    return x  # NOTE: else is not necessary here, ask yourself why?

def absolute_value_wrong(x):
    if x < 0:
        return -x
    if x > 0:
        return x
    # No return for x == 0, returns None unintentionally, so would return None!

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    return math.sqrt(dsquared)

# Test the function
d = distance(1, 2, 4, 6)
print(f"Distance: {d}")
