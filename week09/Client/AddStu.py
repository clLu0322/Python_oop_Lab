class AddStu:
    def __init__(self, socket):
        self.parameters = {'name': "", 'scores': {}}
        self.socket = socket

    def execute(self):
        self.input_name()
        return self.parameters
    
    def input_name(self):
        self.name = input("  Please input a student's name: ")
        self.socket.send_command("query", {"name": self.name})
        #詢問名字是否重複
        if self.socket.wait_response()["status"] == 'Fail': 
            self.parameters["name"] = self.name
            self.input_subject()
        else:
            print("  The name is already exists")
            return
    
    def input_subject(self):
        while True:
            subject = input("  Please input a subject name or exit for ending: ")
            if subject == 'exit':
                break
            self.input_score(subject)
        if self.parameters['scores']: 
            #確保不會只有名字 沒有參數就送出
            self.send_data_to_server()
     
    def input_score(self, subject):
        try:
            score = float(input(f"  Please input {self.name}'s {subject} score or < 0 for discarding the subject: "))
            if score >= 0:
                self.parameters["scores"][subject] = score
        except Exception as e:
            print(e)
        
    def send_data_to_server(self):
        self.socket.send_command("add",self.parameters)
        if self.socket.wait_response()["status"] == 'OK':
            print(f"  Add {self.parameters} success")
        else:
            print(f"  Add {self.parameters} fail")
        