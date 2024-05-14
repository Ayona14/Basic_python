# el1=input("enter your favourite movie: ")
# el2=input("enter another movie: ")
# el3=input("enter another movie: ")
# list1=[el1,el2,el3]
# print("list of your fav movies are: ", list1)

# list2=[1,2,6,4,1]
# list3=list2.copy()
# list3.reverse()
# if(list2 == list3):
#   print("list is palindrome")
# else:
#   print("list is not palindrome")

# tup=("C","D","A","A","B","B","A")
# print(tup.count("A"))

# list1=["C","D","A","A","B","B","A"]
# print(list1)
# list1.sort()
# print("updated list: ",list1)

# dict={
#   "name" : "Ayona sahu",
#   "age":22,
#   "gender":"female",
#   "score":{
#     "maths": 89,
#     "phy": 90,
#     "chem":88
#   }
# }
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get("name")) #doesnt return error on mistakes it rather returns none
# print(dict["name"]) #returns error on mistakes
# dict.update({"location": "Bhubaneswar"})
# print(dict)

nums={1,2,3,4,5,"hello","world"}
print(nums)
nums.add((3,4,5))
nums.add(True)
nums.add("ayona")
print(nums)
nums.remove("hello")
print(nums)
num2={"ayona","sahu","mango","summer"}
print(num2.pop())
print(num2)
nums1=set() #null set
set1={1,2,3,4}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))