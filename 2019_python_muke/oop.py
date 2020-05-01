class Myclass01():
    name = 'lin'
    age = 20 

    def __init__(self,age):
        print("construct excute")

    def getout(self):
        print(self.name)

myclass = Myclass01(1)
myclass.getout()