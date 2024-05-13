import json
from Commands.AddStu import AddStu
from Commands.Query import Query
from Commands.ModifyStu import ModifyStu
from Commands.DelStu import DelStu
from Commands.PrintAll import PrintAll

class Parser:
    def __init__(self, raw_message, address):
        self.address = address
        self.message = json.loads(raw_message)
        self.command = self.message['command']
        self.parameters = self.message['parameters']
        self.action_list = {
                        "add" : AddStu,
                        "show": PrintAll,
                        "query": Query,
                        "modify": ModifyStu,
                        "delete": DelStu
                        }
    
    def parse(self):
        print(self.message)
        server_received = {'command': self.command, 'parameters': self.parameters}
        print(f"    server received: {server_received} from {self.address}")
        send_message = self.action_list[self.command](self.parameters).execute()
        print(send_message)
        return json.dumps(send_message)