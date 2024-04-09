
import client
import socket 
from AddStu import AddStu
from PrintAll import PrintAll
from client import SocketClient


host = "127.0.0.1"
port = 20001

action_list = {
    "add": AddStu, 
    "show": PrintAll
}

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

def main():
    client_main = client.SocketClient(host,port)
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result]().execute(client_main)
        except:
            print("wrong command!!")
main()