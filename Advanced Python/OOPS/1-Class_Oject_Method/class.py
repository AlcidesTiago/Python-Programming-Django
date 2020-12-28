class Student (object):
    def __init__(self):
        self.no = 0
        self.name = ''
        self.marks = 0

    def talk(self):
        s1 = int(input('Hi, my id no is :'))
        s2 = input('My name is :')
        s3 = int(input('My marks are : '))
        print('Congratulations,', s2 + ', you have clear this exam!')


obj = Student()
obj.talk()