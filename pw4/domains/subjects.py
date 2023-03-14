#Create class Subject
class Subject:
    def __init__(self,id_subject: int,name_subject: str):
        self.__id_subject = id_subject
        self.__name_subject = name_subject
    def get_subject(self):
        return f"ID: {self.__id_subject}  Name: {self.__name_subject}"