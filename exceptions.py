import sys
try:
    x=int(input("x:"))
    y=int(input("y:"))
except ValueError:
    print('Error:Only numbers allowed.')
    sys.exit(1)
try:
    res=x/y
except ZeroDivisionError:
    print("Error:Cannot divide by zero")
    sys.exit(1)
print(f"{x}/{y} is {res}")