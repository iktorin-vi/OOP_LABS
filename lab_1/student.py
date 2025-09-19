from lab_1.person import Person

class Student(Person):
    def __init__(self,first_name,last_name,student_id,passport=0,weight=0,height=0):
        super().__init__(first_name, last_name)
        self.student_id=student_id
        self.passport=passport
        self.weight=int(weight)
        self.height=int(height)

    def is_ideal_weight(self):
        return self.height - 110 == self.weight
