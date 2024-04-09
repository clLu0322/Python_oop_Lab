import client
import time
import json

class PrintAll:
    def __init__(self):
        pass
    
    def execute(self, input_client):
        try:
            input_client.send_command_data('show')

            input_client.wait_server()
            
            print ("\n==== student list ====\n")

            input_client.mutex.acquire()
            if input_client.raw_data["status"] == "OK":
                outer_data = input_client.raw_data['parameters']
            else:
                outer_data = {}
            input_client.mutex.release()
            
            for key, iner_data in outer_data.items() :
                print('name: ', iner_data['name'])
                for subject ,score in iner_data['scores'].items():
                    print('     subject: ', subject, 'score: ', score)
                
            print ("======================")

        except Exception as e:
            print(e)