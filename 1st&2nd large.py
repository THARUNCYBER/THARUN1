list1=[ ]
x=int(input("length of the list:"))
for i in range(x):
    val=int(input())
    list1.append(val)
print("list1",list1)
list1.sort()      
print("Enter the largest no in list:",list1[-1])
print("Enter the second largest no in list:",list1[-2])
