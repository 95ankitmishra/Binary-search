print("enter two number")
a,b=int(input()),int(input())
H=min(a,b)
while H>=1:
    if a % H==0 and b % H==0:
        if H==1:
            print("co prime number")
        else:
            print("not co prime")
        break
    H=H-1
