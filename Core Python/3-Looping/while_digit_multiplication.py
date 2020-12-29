mul = 1
n = int(input('Enter num:'))
while n > 0:
    rem = n % 10
    mul = mul * rem
    n = int(n / 10)
print('multiplication=', mul)