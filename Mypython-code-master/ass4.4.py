a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
for x in range(a,b+1):
    for y in range(2,x):
        if x % y==0:
            break
    else:
        print(x)
