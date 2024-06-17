from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class ModifyStu:
    def __init__(self, parameters={}):
        self.parameters = parameters
        self.student_table = StudentInfoTable()
        self.subject_table = SubjectInfoTable()
    
    def execute(self):
        stu_id = self.student_table.select_a_student(self.parameters['name'])
        student_subjects = self.subject_table.get_student_all_subject(stu_id)
        for subject, score in self.parameters['scores'].items():
            if subject in student_subjects:
                self.subject_table.update_student_subject(stu_id, subject, score)
            else:
                parameter = {'name': self.parameters['name'], 'scores': {subject: score}}
                self.subject_table.insert_student_all_subject(stu_id, parameter)
        return {"status": "OK"}