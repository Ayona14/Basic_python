# class car:
#   name="mercedes"
#   color="red"
# car1=car()
# print(car1.name)
# print(car1.color)

class student:
  college="KIIT university"
  def __init__(self):  #default constructor
    pass
  def __init__(self,fullname,marks,age): #parameterized constructor
    self.name=fullname
    self.marks=marks
    self.age=age
  def average(self):
    sum= self.marks[0]+ self.marks[1] + self.marks[2]
    Sum=int(sum)
    avg=Sum/3
    Avg=float(avg)
    A=print(Avg)
    return A
print(student.college)
s1=student("Ayona",[90,89,85],22)
print(s1.name,s1.marks,s1.age)
s1.average()
    
s2=student("Eshna",[94,93,90],21)
print(s2.name,s2.marks,s2.age)
s2.average()

s3=student("Ankit",[89,79,90],20)
print(s3.name,s3.marks,s3.age)
s3.average()

s4=student("Pritam",[90,90,89],15)
print(s4.name,s4.marks,s4.age)
s4.average()