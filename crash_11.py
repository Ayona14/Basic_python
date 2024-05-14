# f=open("ayona.txt","r")
# data=f.readline()
# print(data)
# data1=f.readline()
# print(data1)
# f.close()

# f=open("ayona.txt","w")
# f.write("my name is ayona sahu \n i am studying in KIIT university \n currently in my 4th year pursuring Btech in Information Technology")

# f=open("ayona.txt","a")
# f.write("\ni am at the last year of my college life and it sucks")

# f=open("ayona.txt","r+")
# f.write("Hello \n")

# with open("ayona.txt","w+") as f:
#   data=f.read()
#   print(data)
#   data1=f.write("Hi everyone \n we are learning File 1/0 \n using Java. \nI like programming in Java.")
#   f.close()

with open("ayona.txt","r") as f:
  data=f.read()
  data_new=data.replace("Java","Python")
  f.close()

with open("ayona.txt","w") as f:
  f.write(data_new)
  f.close()