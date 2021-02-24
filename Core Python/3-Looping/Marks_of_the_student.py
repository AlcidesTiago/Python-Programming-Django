Python = int(input('Enter Marks of  Python:'))
Java = int(input('Enter Marks of Java:'))
iOS = int(input('Enter Marks of iOS:'))
JScript = int(input('Enter Marks of JScript:'))
WebT = int(input('Enter Marks of WebT:'))

Total_marks = Python + Java + iOS + JScript + WebT
Percentage = Total_marks/5
if Percentage < 35:
    print('U failed = {}'.format(Percentage))
else:
    print('Congratulation, you pass.')