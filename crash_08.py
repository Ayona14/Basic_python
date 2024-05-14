# def avg(a,b,c):
#   sum=a+b+c
#   Sum=int(sum)
#   avg=sum/3
#   Avg=float(avg)
#   return avg

# print(avg(1,2,3))
# print(avg(1,5,6))
# print(avg(1,9,3))
# print(avg(7,2,3))

def avg(a=4,b=5,c=6):  #default parameters
  sum=a+b+c
  Sum=int(sum)
  avg=sum/3
  Avg=float(avg)
  return avg
op=avg()
print(op)