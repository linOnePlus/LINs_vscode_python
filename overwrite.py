class father():
    sum = 0

    def count(self):
        for x in range(0, 5):
            self.__class__.sum += 1
        return self.__class__.sum 
# a=father()
# print(a.count())
class son(father):
    def count(self):
        a = super(son,self).count()
        print(a)
       


domain = son()
domain.count()

