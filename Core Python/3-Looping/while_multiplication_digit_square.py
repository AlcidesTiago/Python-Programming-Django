ans = 1
n = int(input('Enter num:'))
while n > 0:
    rem = n % 10
    ans = ans * (rem * rem)
    n = int(n / 10)
print('ans=', ans)