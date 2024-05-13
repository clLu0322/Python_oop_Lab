from DBController.StudentInfoTable import StudentInfoTable
from DBController.SubjectInfoTable import SubjectInfoTable

class PrintAll:
    def __init__(self, parameters={}):
        self.parameters = parameters
        self.student_table = StudentInfoTable()
        self.subject_table = SubjectInfoTable(parameters)

    def execute(self):
        student_name_list = self.student_table.get_all_student()
        return_message = {"status": "OK", "parameters": {}}
        for student_name in student_name_list:
            stu_id = self.student_table.select_a_student(student_name)
            student_subjects = self.subject_table.get_student_all_subject(stu_id)
            if len(student_subjects) != 0:
                return_message["parameters"].update(
                    {student_name: {"name": student_name, "scores": student_subjects}}
                )
        return return_message