import math
# Create class Avarage GPA for student
class avg_gpa:
    def __init__(self,gpa: float):
        self.gpa = gpa
    def get_avg_gpa(self):
        return f"{round(self.gpa,2)}"