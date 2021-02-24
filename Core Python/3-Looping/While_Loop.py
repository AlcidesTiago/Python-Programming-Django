# While_Loop
n = int(input('Enter a Number :'))
total = 0
while n > 0:
    rem = n % 10
    total = total + rem
    n = int(n / 10)
print('Total ', total)