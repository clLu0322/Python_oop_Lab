from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class Query:
    def __init__(self, parameters={}):
        self.parameters = parameters
        self.student_table = StudentInfoTable()
        self.subject_table = SubjectInfoTable(parameters)

    def execute(self):
        stu_id = self.student_table.select_a_student(self.parameters['name'])
        if not stu_id:
            return {"status": "Fail", "reason": "The name is not found."}
        else:
            student_subjects = self.subject_table.get_student_all_subject(stu_id)
            return {"status": "OK", "scores": student_subjects}