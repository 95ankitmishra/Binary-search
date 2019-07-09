def Lcm(a,b):
    L=max(a,b)
    while(L<=a*b):
        if((L%a==0)and (L%b==0)):
            Lcm=L
            break
        L=L+1
    return Lcm
print("enter two number")
x,y=eval(input())
print("lcm of two number is",Lcm(x,y))
