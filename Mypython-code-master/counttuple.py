val=tuple(int(x) for x in input("enter tuple elements").split(','))
s=0
for e in val:
    s=s+e
print("sum is ",s)
#s=sum(val)
#print("sum of  tuple",s) 
