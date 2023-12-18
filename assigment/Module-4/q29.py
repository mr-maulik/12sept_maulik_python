# What relationship is appropriate for Course and Faculty? 

class Faculty: 
    def subject(self):
        print("The faculty is python..")

class Course (Faculty): 
    def chapter(self):
        print("The Course is full-stack python..")

fc = Course() 
fc.subject()
fc.chapter()