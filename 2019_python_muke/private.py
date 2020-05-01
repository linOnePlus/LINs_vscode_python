class testprivate():
    __name =''
    @classmethod
    def funcname(cls, name):
        if name != '':
            cls.name = name
            print(cls.name)
obj = testprivate()
name2=input()
obj.funcname(name2)
# print(testprivate.__name) 私有了不能打印

