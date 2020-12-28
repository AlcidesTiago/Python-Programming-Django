'''
1. Compile Time.
    # e.g:. Method Overloading
    -Function = same
    -Class name = same
    -Argument/Parameter = different
'''

# 1. Compile Time.
#     # e.g:. Method Overloading

''' Python does not support bellow type of method/code, instead they use if, else, statement logic '''
# e.g:. Method Overloading (v.1)
# class A:
#     def add(self, a, b):
#         sum = a +  b
#         print(sum)
#
#
#     def add(self, a, b, c):
#         sum = a + b + c
#         print(sum)


# obj = A()
# obj.add(10, 20)

class A:
    def add(self, a, b, c=None):
        if c is None:
            sum = a + b
            print(sum)
        else:
            sum = a + b + c
            print(sum)


obj = A()
obj.add(10, 20, 30)