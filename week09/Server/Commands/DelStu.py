from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class DelStu:
    def __init__(self, parameters={}):
        self.parameters = parameters
        self.student_table = StudentInfoTable()
        self.subject_table = SubjectInfoTable()
    
    def execute(self):
        stu_id = self.student_table.select_a_student(self.parameters["name"])
        self.student_table.delete_a_student(stu_id)
        self.subject_table.del_student_all_subject(stu_id)
        return {"status": "OK"}