from person import Person
class Student(Person):
    def __init__(self, id: int,name: str,dob: str):
        super().__init__(name)
        self.__name = name
        self.__id = id
        self.__dob = dob
    def get_student(self):
        return f"ID: {self.__id}  Name: {self.__name}  DOB: {self.__dob}"