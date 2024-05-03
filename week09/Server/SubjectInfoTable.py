from DBConnection import DBConnection

class SubjectInfoTable:
    def __init__(self, parameter={}):
        self.student_dict = parameter
        
    def insert_student_all_subject(self, stu_id):
        with DBConnection() as connection:
            cursor = connection.cursor()
            for subject, score in self.student_dict.get("scores" , {}).items():
                command = f"INSERT INTO subject_info (stu_id, subject, score) VALUES ('{stu_id}', '{subject}', {score});"
                cursor.execute(command)
            connection.commit()
    
    def get_student_all_subject(self, stu_id):
        command = f"SELECT * FROM subject_info WHERE stu_id='{stu_id}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        return_message = {row["subject"]: row["score"] for row in record_from_db}
        return return_message
    
    def del_student_all_subject(self, stu_id):
        command = f"DELETE FROM subject_info WHERE stu_id='{stu_id}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
    
    def update_student_subject(self, stu_id):
        #更新學生科目
        command = f"UPDATE subject_info SET subject='{self.student_dict['scores'].keys()}' WHERE stu_id = {stu_id}"