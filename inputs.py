import sys

# using exceptions
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid number!")
    sys.exit(1)

# using conditions
if (num > 0):
    print("Number is positive.")
elif (num < 0):
    print("Number is negative.")
else:
    print("Number is zero...")
    