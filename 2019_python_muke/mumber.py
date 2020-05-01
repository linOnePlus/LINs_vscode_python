class Mumber():
    name = "" 
    age = 0

    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def getinfo(self): # 传self
        print(self.name +str(self.age))

mumber = Mumber('lin',18)
mumber.getinfo()
