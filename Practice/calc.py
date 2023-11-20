import math
class calc():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sum(self):
        return self.x+self.y
    def div(self):
        return self.x/self.y
    def multi(self):
        return self.x*self.y

class minus(calc):
    def min(self):
        return self.x-self.y

x=int(input()) 
y=int(input())        
c=minus(x,y)
print(c.min())
print(c.sum())
print(c.div())
print(c.multi())


