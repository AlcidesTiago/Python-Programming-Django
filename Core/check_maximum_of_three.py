# check maximum of three number
num1 = int(input('enter num1:'))
num2 = int(input('enter num2:'))
num3 = int(input('enter num3:'))
if (num1 > num2) and (num1 > num3):
    print('num1 greater')
elif (num2 > num1) and (num2 > num3):
    print('num2 greater')
elif(num3 > num1) and (num3 > num2):
    print('num3 greater')