'''
Polymorphism means poly (many) + morphirm(form)
There are two types of polymorphism;
1. Compile Time.
    # e.g:. Method Overloading
2. Runtime
    # e.g:. Method Overriding   (most important)

                Explanations:
1. Compile Time.
    # e.g:. Method Overloading
    -Function = same
    -Class name = same
    -Argument/Parameter = different


2. Runtime
    # e.g:. Method Overriding   (most important)
    -Function = same
    -Class name = different
    -Argument/Parameter = same
'''
# 1. Compile Time.
#     # e.g:. Method Overloading

''' 
Python does not support bellow type of method/code, instead they use if, else, statement logic 
'''
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

'''Python created bellow form for handle this situation'''
# e.g:. Method Overloading (v.2)
# class A:
#     def add(self, a, b, c=None):
#         if c is None:
#             sum = a + b
#             print(sum)
#         else:
#             sum = a + b + c
#             print(sum)
#
#
# obj = A()
# obj.add(10, 20, 30)

# 2. Runtime
#     e.g:. Method Overriding   (most important)

class A:
    def hello(self):
        print("I am Hello From A Class")

    def demo(self):
        print("I am Demo From A Class")


class B(A):
    def hello(self):
        print("I am Hello From B Class")


obj = B()
obj.hello()

