from DBConnection import DBConnection

class SubjectInfoTable:
    def __init__(self, parameter={}):
        self.student_dict = parameter
        
    def insert_student_all_subject(self, student_id):
        with DBConnection() as connection:
            cursor = connection.cursor()
  
            for subject, score in self.student_dict.get("scores" , {}).items():
                command = "INSERT INTO subject_info (stu_id, subject, score) VALUES ('{}', '{}', {});".format(
                    student_id, subject, score
                )
                cursor.execute(command)
            connection.commit()
    
    def get_student_all_subject(self, student_id):
        command = "SELECT * FROM subject_info WHERE stu_id='{}';".format(student_id)
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        return_message = {row["subject"]: row["score"] for row in record_from_db}
        return return_message
    
    def del_student_all_subject(self, student_id):
        command = "DELETE FROM subject_info WHERE stu_id='{}';".format(student_id)
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()