names=[]
n=int(input("how many names you want to be stored"))
for i  in range(n):
    print(i+1,"enter names")
    names.append(input())
s=set(names)
names=list(s)
print(names)
