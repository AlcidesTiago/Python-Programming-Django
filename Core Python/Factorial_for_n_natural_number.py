#Find the factorial of any natural number

number = int(input("\nEnter a number : "))
factorial = 1

if number < 0:
    print("The factorial of 0 is 1.")
elif number == 0:
    print("Sorry, enter a positive number.")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("The factorial of", number, "is", factorial)