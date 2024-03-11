def main(student_list):
    try:
        name = input("  Please input a student's name: ")
        
        # 檢查名字是否已經存在於學生列表中
        for student in student_list:
            if student[0] == name:
                print(f"  The name {name} already exists.")
                return  # 名字已存在，直接返回，不執行後續程式碼
        
        score = float(input(f"  Please input {name} score: "))
        
        student_list.append([name, score])
        print(f"  Add [{name}, {score}] success")
    except ValueError:
        print("Invalid input! Please enter a valid score as a number.")











