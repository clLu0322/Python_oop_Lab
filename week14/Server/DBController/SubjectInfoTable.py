from DBController.DBConnection import DBConnection

class SubjectInfoTable:
    # def insert_a_subject(self, stu_id, subject, score):
    #     command = f"INSERT INTO subject_info (stu_id, subject, score) VALUES ('{stu_id}', '{subject}', {score});"
    #     with DBConnection() as connection:
    #         cursor = connection.cursor()
    #         cursor.execute(command)
    #         connection.commit()
        
    def insert_student_all_subject(self, stu_id, parameter):
        #插入所有學生科目
        with DBConnection() as connection:
            cursor = connection.cursor()
            for subject, score in parameter['scores'].items():
                command = f"INSERT INTO subject_info (stu_id, subject, score) VALUES ('{stu_id}', '{subject}', {score});"
                cursor.execute(command)
            connection.commit()
    
    def get_student_all_subject(self, stu_id):
        #找到學生所有科目，回傳字典
        command = f"SELECT * FROM subject_info WHERE stu_id='{stu_id}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        return_message = {row["subject"]: row["score"] for row in record_from_db}
        return return_message
    
    def del_student_all_subject(self, stu_id):
        #刪除學生所有科目
        command = f"DELETE FROM subject_info WHERE stu_id='{stu_id}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
    
    def update_student_subject(self, stu_id, subject, score):
        #更新學生科目
        command = f"UPDATE subject_info SET score='{score}' WHERE stu_id='{stu_id}' AND subject='{subject}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
    