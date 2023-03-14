#Create class Mark
class Mark:
    def __init__(self,mark: float):
        self.__mark = mark
    def get_mark(self):
        return f"{self.__mark}"