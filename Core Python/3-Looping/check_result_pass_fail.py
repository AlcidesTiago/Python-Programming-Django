# calculate percentage and total marks & check student is pass or fail
maths = int(input('enter mark of maths:'))
eng = int(input('enter mark of english:'))
sci = int(input('enter mark of science:'))
com = int(input('enter mark of computer:'))
phy = int(input('enter mark of physics:'))
total = int(maths + eng + sci + com + phy)
print('total=', total)
per = float(total / 5)
print('percentage', per, '%')
print('Congratulation you got {} total mark and {} percentage'.format(total, per))
if per < 35.0:
    print('fail!!!')
elif per:
    print('pass...')