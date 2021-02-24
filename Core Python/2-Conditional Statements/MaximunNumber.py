#     3 maximun
a = int(input('Enter First value:'))
b = int(input('Enter Second value:'))
c = int(input('Enter Third value:'))
if a < b:
    if a > c:
        print('A is Big')
    else:
        print('C is Big')
elif a == b:
    if b > c:
        print('B is Big')
    else:
        print('C is Big.')