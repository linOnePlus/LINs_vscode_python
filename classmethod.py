class testclassmethod:
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sum+=1

    @classmethod
    def countSum(cls):
        # testclassmethod.sum += 1
        cls.sum+=1

    @staticmethod
    def teststatic(a,b):
        print("hellostaticmethod")


stu1 = testclassmethod("lin", 11)
testclassmethod.countSum()
print(testclassmethod.sum)
testclassmethod.teststatic(1,2)
