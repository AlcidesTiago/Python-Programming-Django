class Python_students:
    __s_id = 0
    __s_name = ''

    def set_students(self, id, name):
        self.__s_id = id
        self.__s_name = name

    def get_stufdents(self, id, name):
        print(self.__s_id)
        print(self.__s_name)


id = int(input('Enter student id: '))
name = input('Enter student name: ')

# object of class
obj = Python_students()
obj.get_stufdents(id, name)
obj.get_stufdents()
