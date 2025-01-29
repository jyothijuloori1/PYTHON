#1.An empty list
L1=[]
print("An empty list",L1)
#2. A list with four items(indexs 0-3)
L2=[0,1,2,3]
print("List with four items",L2)
#3.Nested list
L3=['abc',['def','ghi']]
print("A nested list",L3)
#creating a list froem string
L4=list('spam')
print("List created from string 'spam",L4)
#creating a list from a range of integers
L5=list(range(-4,4))
print("List created from range(-4,4)",L5)
# accessing an element by index
L6=[10,20,30,40]
print("element at index 2 of L6",L6[2])
#Accessing an element from nested list by index
L7=['x',[10,20,30],'y']
print("Element at L7[1][2] (nested list):",L7[1][2])
# slicing a list
L8=[0,1,2,3,4,5]
print("Slicing L8 from index 2 to 4 (L8[2:5])",len(L8))
#getting the length of a list
L9=[10,[100,200,300,400],50]
print("Element at L9[1]",L9[1])# access the subset 
print("Element at L9[1][3]",L9[1][3])#access element 3 from the sublist
print("Slicing submit L9[1][1:3]:",L9[1][1:3])
#demonstrate nested indexing and slicing together
# summary of output
print("\nSummary of lists:")
print("L1:",L1)
print("L2:",L2)
print("L4:",L4)
print("L5:",L5)
print("L6:",L6)
print("L7:",L7)
print("L8:",L8)
print("L9:",L9)
#basic use of list
print(len([1,2,3]))
combinedlist=[1,2,3]+[4,5,6]
print(combinedlist)

sameValueList=['abc']*4
print(sameValueList)

print(str([1,2])+"34") #same as "[1,2]" + "34"

print([1,2]+list("34"))