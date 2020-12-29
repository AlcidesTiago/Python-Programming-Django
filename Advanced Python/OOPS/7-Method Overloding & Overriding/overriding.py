'''
2. Runtime
    # e.g:. Method Overriding   (most important)
    -Function = same
    -Class name = different
    -Argument/Parameter = same
'''

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

