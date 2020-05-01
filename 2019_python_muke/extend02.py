from extend01 import father


class son(father):
    def __init__(self):
        super(son, self).__init__()
        print("son 's construct ")

    def testfather(self):
        self.setfname("lin")
        print(self._father__fname)
        print(super(son, self).sum)
        print("son's method ")
        self.getfname()


s = son()
s.testfather()
