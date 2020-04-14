class father():
    sum = 100
    __fname = ""

    def __init__(self):
        print("father's construct")

    def setfname(self, fname):
        self.__fname = fname
    def getfname(self):
        print(self.__fname)


