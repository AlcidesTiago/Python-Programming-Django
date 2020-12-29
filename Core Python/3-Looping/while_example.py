# example 1
def sum_of_digit():
    total = 0
    n = int(input('Enter number: '))
    while n > 0:
        rem = n % 10
        total += rem
        n = int(n / 10)
    return total


# example 2
def multiplication_of_digit():
    total = 1
    n = int(input('Enter number: '))
    while n > 0:
        rem = n % 10
        total *= rem
        n = int(n / 10)
    return total


# example 3
def sum_of_squares():
    total = 0
    n = int(input('Enter number: '))
    while n > 0:
        rem = n % 10
        square = rem * rem
        total += square
        n = int(n / 10)
    return total


# example 4
def sum_of_cubes():
    total = 0
    n = int(input('Enter number: '))
    while n > 0:
        rem = n % 10
        cube = rem * rem * rem
        total += cube
        n = int(n / 10)
    return total


# example 5
def multiplication_of_squares():
    total = 1
    n = int(input('Enter number: '))
    while n > 0:
        rem = n % 10
        square = rem * rem
        total *= square # total = total * square
        n = int(n / 10)
    return total


# example 6
# number that is equal to he sum of its cubes
def armstrong():
    total = 0
    n = int(input('Enter number: '))
    check = n
    while n > 0:
        rem = n % 10
        cube = rem * rem * rem
        total += cube
        n = int(n / 10)
    if total == check:
        print('Armstrong')
        return 0
    else:
        print('Not Armstrong')
        return 1


# example 7
def reverse_number(n):
    total = 0
    while n > 0:
        rem = n % 10
        total = total * 10 + rem
        n = int(n / 10)
    return total


# example 8
def palindrome():
    n = int(input("Enter number: "))
    if n == reverse_number(n):
        print('Palindrome')
    else:
        print('Not palindrome')

