class PrintAll:
    
    def execute(self, data):

        print ("\n==== student list ====\n")
        for index, value in data.items():
            print(f"Name: {index}")
            for subject, score in value.items():
                print(f"  subject: {subject}, score: {score}")
                print()
        print ("======================")
