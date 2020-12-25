num = int(input('enter num:'))
if num % 5 == 0:
    if num % 3 == 0:
        print('divisible by 5 & 3')
    else:
        print('divisible by only 5')
else:
    print('not divisible by 5')