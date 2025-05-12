class parent:
    def area(self,a,b=None):
        if b==None:
            return a*a
        else:
            return a*b
c1 = parent()
result1 = c1.area(10)
print(result1)