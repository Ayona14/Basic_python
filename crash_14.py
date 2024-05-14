class A:
  val="welcome to class A"
class B:
  valB="welcome to class B"
class C(A,B):
  valC="welcome to class C"
c=C()
print(c.val)
print(c.valB)
print(c.valC)