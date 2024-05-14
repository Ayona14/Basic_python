class student:
  def __init__(self,phy,chem,maths):
    self.phy=phy
    self.chem=chem
    self.maths=maths
    # self.percentage=str((self.phy+self.chem+self.maths)/3)
  # def cal_percentage(self):
  #   self.percentage=str((self.phy + self.chem + self.maths)/3)
  @property
  def calculate(self):
    return str((self.phy + self.chem + self.maths)/3)

st1=student(98,90,89)
print(st1.calculate)

st1.phy=88
print(st1.calculate)