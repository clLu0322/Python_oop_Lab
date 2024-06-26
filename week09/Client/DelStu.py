class DelStu:
    def __init__(self,socket):
        self.socket = socket
    
    def execute(self):
        self.input_name()

    def input_name(self):
        name = input("  Please input a student's name: ")
        self.socket.send_command("query", {"name": name})
        #詢問名字是否重複
        if self.socket.wait_response()["status"] == 'OK': 
            self.conform_del(name)
        else:
            print("  The name is not found")
            return
        
    def conform_del(self, name):
        if input("Confirm to delete (y/n): ").lower() == "y":
            self.socket.send_command("delete",{"name": name})
            if self.socket.wait_response()["status"] == "OK":
                print("\tDelete success")
            else:
                print("\tDelete fail")
        else:
            print(" Undelete")