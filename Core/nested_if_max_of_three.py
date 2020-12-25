# check maximum of three number
num1 = int(input('enter num1:'))
num2 = int(input('enter num2:'))
num3 = int(input('enter num3:'))
if num1 > num2:
    if num1 > num3:
        print('num1 is greater')
    else:
        print('num 3 is greater')
else:
    if num2 > num3:
        print('num2 is greater')
    else:
        print('num3 is greater')