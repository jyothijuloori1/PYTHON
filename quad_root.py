import math
a=float(input())
b=float(input())
c=float(input())
root1=(-b+math.sqrt(b*b-4*a*c))//2*a
root2=(-b-math.sqrt(b*b-4*a*c))//2*a
print(root1,root2)
