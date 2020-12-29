ans = 0
n = int(input('Enter num:'))
a = n
while n > 0:
    rem = n % 10
    ans = ans + (rem * rem * rem)
    n = int(n / 10)
print('ans=', ans)
if a == ans:
    print('number is armstrong')
else:
    print('number is not armstrong')