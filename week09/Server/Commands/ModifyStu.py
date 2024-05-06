from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class ModifyStu:
    def __init__(self, parameters={}):
        self.parameters = parameters
        self.student_table = StudentInfoTable()
        self.subject_table = SubjectInfoTable(parameters)
    
    def execute(self):
        stu_id = self.student_table.insert_a_student(self.parameters['name'])
        student_subjects = self.subject_table.get_student_all_subject(stu_id)
        for subject, score in self.parameters['scores'].items():
            if subject in student_subjects:
                self.subject_table.update_student_subject(stu_id, subject, score)
            else:
                self.subject_table.insert_a_subject(stu_id, subject, score)
        return {"status": "OK"}