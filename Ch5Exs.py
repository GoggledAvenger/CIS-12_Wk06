# Chapter 5 Exercises

# Ex top of pg 69

from time import time

now = int(time())
mins, seconds =  divmod(now, 60)
hours, mins = divmod(mins, 60)
days, hours = divmod(hours, 24)
print(f'Time since the Unix Epoch has been {days} days, {hours} hours, {mins} minutes, and {seconds} seconds.')

# Ex middle of pg 69

def is_triangle(a,b,c):
    if a > b + c:
        return False
    elif b > c + a:
        return False
    elif c > a + b:
        return False

print(is_triangle(4,3,5))






