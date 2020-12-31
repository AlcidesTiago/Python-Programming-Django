class Dog:
    kind = 'kanine'         # class variable shared by all instances
    '''A simple example class'''

    def __init__(self,name):
        self.name = name
        print(name)