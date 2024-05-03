import socket 
import json
BUFFER_SIZE = 1940

host = "127.0.0.1"
port = 20001

class SocketClient:
    def __init__(self, host= host, port=port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
 
    def send_command(self, command, parameters):
        send_data = {'command': command, 'parameters': parameters}
        self.client_socket.send(json.dumps(send_data).encode())

        #因為demo中 command為modify時，會print出scores_dict而非原本的scores
        if command == 'modify':
            for key, value in send_data.items():
                if key == 'parameters':
                    new_parameters = {}
                    for key2, value2 in value.items():
                        if key2 == 'scores':
                            new_parameters['scores_dict'] = value2
                        else:
                            new_parameters[key2] = value2
                    send_data[key] = new_parameters
        print(f"    The client sent data => {send_data}")

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode()
        print(f"    The client received data => {raw_data}")
        return json.loads(raw_data)

"""
    if __name__ == '__main__':
    client = SocketClient(host, port)

    keep_going = True
    while keep_going:
        command = input(">>>")
        client.send_command(command)
        keep_going = client.wait_response() 
"""