class mlops:
    def __init__(self, totalStudents):
        self.totalStudents = totalStudents

    def getTotalStudents(self):
        return self.totalStudents
    
    def addStudents(self):
        self.totalStudents = self.totalStudents + 1
    
    def removeStudent(self):
        self.totalStudents = self.totalStudents - 1

    def getClassName(self):
        return "Machine Learning Operations (CS-B)"

