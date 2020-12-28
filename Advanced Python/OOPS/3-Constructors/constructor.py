class Python_students:
    __s_id = 0
    __s_name = ''

    def __init__(self, id, name):
        self.__s_id = id
        self.__s_name = name

    def get_stufdents(self):
        print(self.__s_id)
        print(self.__s_name)

id = int(input('Enter student id: '))
name = input('Enter student name: ')


obj = Python_students(id, name)
obj.get_stufdents()
