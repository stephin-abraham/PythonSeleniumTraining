from oopsDemo import oops

class Child(oops):
    def newData(self,n):
        print(n)

ob=Child()
ob.calculator(17,6)
ob.newMethod()
ob.newData(10)
