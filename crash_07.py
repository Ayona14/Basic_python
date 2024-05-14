# list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# number=int(input("enter a number"))
# i=0
# for val in list:
#   if(val == number):
#     print(number,"found at",i)
#   i+=1

# number=int(input("enter a number: "))
# for i in range(1,11):
#   print(number*i)
n=int(input("enter a number n: "))
i=1
sum=1
while i <= n:
  sum=sum*i
  i+=1
print(sum)
  