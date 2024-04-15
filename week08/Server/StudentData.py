import pickle
class StudentInfoProcessor:
    def __init__(self, parameters = {}):
        self.student_dict = dict()
        self.parameters = parameters

    def read_student_file(self):
        self.student_dict = dict()
        try:
            with open("student_dict.db", "rb") as fp:
                self.student_dict = pickle.load(fp)
        except:
            pass

    def restore_student_file(self):
        with open("student_dict.db", "wb") as fp:
            pickle.dump(self.student_dict, fp)
    
    def add(self):
        self.read_student_file()
        std_name = self.parameters['name']
        std_subject_dict = self.parameters['score']

        if std_name in self.student_dict:
            return {'status': 'Fail', 'reason': 'The name already exists.'}
        else:
            self.student_dict[std_name] = std_subject_dict

        self.restore_student_file()
        return {'status': 'OK'}
    
    def show(self):
        self.read_student_file()
        reply_message = {'status': 'OK', 'parameters': {}}
        if not self.student_dict:
            #沒有資料
            reply_message['parameters'] = {}
        else:
            for std_name, std_subject_dict in self.student_dict.items():
                reply_message['parameters'].update({std_name: {'name': std_name, 'scores': std_subject_dict}})
        return reply_message