# string variable
name = "Samuel P. de Leon"
print("Hello " + name + "!")

# array in python
names = ["Harry", "Ron", "Tess", "Meghan"]

for x in names:
    print(x)

# int variable
x = 1
# concatenate string + string
if x == 1:
    print("x = " + str(x))

# float variable
y = 5.0
print(y)
z = float(27)
print(z)

a, b = 3, 4
print(a,b)

if name == "Test":
    print("String: %s" % name)
if isinstance(y, float) and y == 10.0:
    print("Float: %f" % y)
if isinstance(x, int) and x == 1:
    print("Int %d" % x)
