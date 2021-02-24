# swapping without using third variable
num_1 = int(input('enter first number:'))
num_2 = int(input('enter second number:'))
print('before swapping....................')
print('num_1=', num_1)
print('num_2=', num_2)
num_1 = num_1 * num_2
num_2 = num_1 / num_2
num_1 = num_1 / num_2
print('after swapping.....................')
print('num_1=', num_1)
print('num_2=', num_2)