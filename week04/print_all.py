def main(student_dict):
    print ("\n==== student list ====\n")
    for index, value in student_dict.items():
        print(f"Name: {index}")
        for subject, score in value.items():
            print(f"  subject: {subject}, score: {score}")
            print()
    print ("======================")
