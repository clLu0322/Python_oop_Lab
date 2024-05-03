from DBConnection import DBConnection

class StudentInfoTable:
    def insert_a_student(self, name):
        #新增學生姓名
        command = f"INSERT INTO student_info (name) VALUES  ('{name}');"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
        return self.select_a_student(name)

    def select_a_student(self, name):
        #查詢學生的id
        command = f"SELECT * FROM student_info WHERE name='{name}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        if not record_from_db:
            return None
        else:
            return [row["stu_id"] for row in record_from_db][0]

    def delete_a_student(self, stu_id):
        #刪除學生
        command = f"DELETE FROM student_info WHERE stu_id='{stu_id}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def get_all_student(self):
        command = "SELECT name FROM student_info"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        all_student_name = [row[0] for row in record_from_db]
        return all_student_name
    
    

    def update_a_student(self, stu_id, name):
        #更新學生姓名
        command = f"UPDATE student_info SET name='{name}' WHERE stu_id='{stu_id}';"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

