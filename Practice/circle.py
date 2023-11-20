from datetime import date
class circle:
    def __init__(self,r):
        self.Radius=r
        print(3.14*self.Radius*self.Radius)
    
c=circle(2)

class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    
    def age(self):
        today=date.today()
        Age=today.year-self.dob.year
        if today<date(today.year, self.dob.month, self.dob.day):
            Age -= 1
        return Age

p1=person("sagar",'india',date(1994,2,8))
print("name",p1.name)
print("country",p1.country)
print("dob",p1.dob)
print("Age",p1.age())

