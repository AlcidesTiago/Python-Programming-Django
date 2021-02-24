# 4. Swapping without using 3rd variable
a = int(input('Enter the First Number:'))
b = int(input('Enter the Secund Number:'))

a = a + b
b = a - b
a = a - b

print('Value of A {}'.format(a))
print('Value of B {}'.format(b))
