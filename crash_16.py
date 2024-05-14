class person:
  name="anannya"

  @classmethod
  def changeName(cls,name):
    cls.name=name

p1=person()
p1.changeName("Ayona")
print(p1.name)
print(person.name)