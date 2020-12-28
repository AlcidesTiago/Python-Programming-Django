add = 0
n = int(input('Enter num:'))
while n > 0:
    rem = n % 10
    add = add + rem
    n = int(n / 10)
print('addition=', add)