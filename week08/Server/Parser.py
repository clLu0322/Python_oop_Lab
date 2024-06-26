import json
from StudentData import StudentInfoProcessor

class Parser:
    def __init__(self, raw_message, address):
        self.address = address
        self.message = json.loads(raw_message)
        self.command = self.message['command']
        self.parameters = self.message['parameters']
        self.action_list = {
                        "add" : StudentInfoProcessor(self.parameters).add,
                        "show": StudentInfoProcessor(self.parameters).show}
    
    def parse(self):
        print(self.message)
        server_received = {'command': self.command, 'parameters': self.parameters}
        print(f"    server received: {server_received} from {self.address}")
        send_message = self.action_list[self.command]()
        return json.dumps(send_message)