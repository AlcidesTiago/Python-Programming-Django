a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))

print("Before swapping:")
print("Value of a:", a)
print("Value of b:", b)


a = a * b
b = a / b
a = a / b

print("After swapping:")
print("Value of a:", int(a))
print("Value of b:", int(b))
