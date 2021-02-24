rev = 0
n = int(input('Enter num:'))
while n > 0:
    rem = n % 10
    rev = (rev * 10) + rem
    n = int(n / 10)
print('reverse=', rev)