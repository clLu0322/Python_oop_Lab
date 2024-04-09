import json
import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 20001
BUFFER_SIZE = 1940



class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

        self.raw_data = {'status': 'Fail', 'parameters': {}}

        self.lock = False
        self.mutex = threading.Lock()
        wait_response_thread = threading.Thread(target=self.wait_response, daemon=True)
        wait_response_thread.start()

    def send_command_data(self, command, data = dict()):
        send_data = {'command': command, 'parameters': data}
        print('The client sent data =>', send_data)
        self.client_socket.send(json.dumps(send_data).encode())

        self.mutex.acquire()
        self.raw_data = {'status': 'Fail', 'parameters': {}}
        self.lock = True
        self.mutex.release()
        

    def send_data(self, data):
        send_data = {data['name'] : data}
        self.client_socket.sned(json.dumps(send_data).encode())

    def wait_response(self):
        while True:
            data = self.client_socket.recv(BUFFER_SIZE)

            self.mutex.acquire()
            self.raw_data = json.loads(data.decode())
            self.lock = False
            self.mutex.release()

            print("The client received data =>", self.raw_data)

            if self.raw_data == "closing":
                exit()

    def release_key(self):
        self.lock = False
        self.mutex.release()

    def wait_server(self):
        cnt = 0
        while self.lock == True:
            time.sleep(1)
            cnt += 1
            if cnt >= 2:
                print("no ACK from sever")
                return

if __name__ == '__main__':
    client = SocketClient(HOST, PORT)

    keep_going = True
    while keep_going:
        command = input(">>>")
        client.send_command(command)
        keep_going = client.wait_response()