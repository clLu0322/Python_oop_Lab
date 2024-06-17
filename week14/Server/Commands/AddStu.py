from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class AddStu:
    def __init__(self, parameters={}):
        self.parameters = parameters
        self.student_table = StudentInfoTable()
        self.subject_table = SubjectInfoTable()

    def execute(self):
        stu_id = self.student_table.insert_a_student(self.parameters["name"])
        self.subject_table.insert_student_all_subject(stu_id, self.parameters)
        return {"status": "OK"}

