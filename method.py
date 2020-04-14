def testmethod():
    print("hello method")


testmethod()

a = 100
b = 120


def testreturndouble(a, b):
    c = a / 2
    d = b * 3
    return c, d


result = testreturndouble(a, b)
print(type(result))

def testname(a=1,b=2):
    print(a,b)
def testname2(a,b):
    print(a,b)
testname()
testname2(b=1,a=2)