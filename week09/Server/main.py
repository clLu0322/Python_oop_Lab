from SocketServer import SocketServer
from DBController.DBConnection import DBConnection
from DBController.DBInitializer import DBInitializer

host = "127.0.0.1"
port = 20001

if __name__ == "__main__":
    DBConnection.db_file_path = "student_dict.db"
    DBInitializer().execute()
    server = SocketServer(host, port)
    server.daemon = True
    server.serve()
    while True:
        command = input()
        if command == "finish":
            break
    server.server_socket.close()
    print("leaving ....... ")