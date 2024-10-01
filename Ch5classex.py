# Exercise 1: Modulus Operator Write a program that checks whether a number
# is divisible by both 3 and 5

def modopex(n):
    return n % 3 == 0 and n % 5 == 0
try:
    number = int(input("Give me a number:"))
    print(modopex(number))
except ValueError as ve:
    print("Not a valid number.")

# Exercise 2: Recursion: Write a recursive function that prints the sum of
# all integers from 1 to n.

def recusum(n):
    if n <= 1:
        return 1
    return n + recusum(n-1)

print(recusum(5))

#Exercise 3: User Input with Error Handling: Ask the user for two integers
# and divide them. Handle errors like division by zero.

x = int(input("Please enter an integer:"))
y = int(input("Please enter another number:"))
print(int(x/y))

def get_ints(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("That is not an integer.")
        except KeyboardInterrupt:
            return

x = get_ints("Please enter integer:")
y = get_ints("Please enter another integer:")

if y == 0:
    print("Zero is invalid.")
else:
    print(int(x/y))


