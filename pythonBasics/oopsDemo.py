#classes are user defined blueprint or prototype
#sum, multiplication, addition, constant
#methods, class variabls instance variables,constructor etc
from tkinter.font import names


class oops:
    def newMethod(self):
        print("Hi all")

    def calculator(self,a,b):
        c=a * b
        print(c)

#create object for a class
obj= oops()
obj. newMethod()
obj.calculator(12,6)
