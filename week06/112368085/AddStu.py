import SocketClient as Client
"""
format of student_info:
ex. {"name": "Bill",
"scores": {"python": 80.0, "english": 90.0}}
"""
class AddStu:
    def __init__(self, client: Client.SocketClient):
        self.client = client
        self.student_info = dict()

    def execute(self):
        name = input("  Please input a student's name or exit: ")
        if name == "exit":
            return
        
        has_scores = self.add_subject(name)
        if has_scores is True:
            self.client.send_command("add", self.student_info)
            raw_data = self.client.wait_response()
            if raw_data["status"] == "OK":
                print(f"    Add {self.student_info} sucess")
            else:
                print(f"    Add {self.student_info} fail")
        else:
            print(f"    Add nothing")

    def add_subject(self, name):
        score_dict = dict()

        while 1: # input subject name
            subject = input("  Please input a subject name or exit for ending: ")
            if subject == "exit":
                break
            elif subject in score_dict:
                print(f"    {subject} already exists")
            else:
                while 1: # input subject score
                    try:
                        score = float(input(f"  Please input {name}'s {subject} score or < 0 for discarding the subject: "))
                    except Exception as e:
                        print(f"    Wrong format with reason {e}, try again")
                    else:
                        if score >= 0:
                            score_dict[subject] = score
                        break

        if len(score_dict) > 0:
            self.student_info = {
                "name": name,
                "scores": score_dict
            }
            return True # 分數欄不為空
        return False