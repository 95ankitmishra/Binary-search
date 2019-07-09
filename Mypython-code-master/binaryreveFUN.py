def bina(num):
    x=bin(num)
    s=x[::-1]
    print("reverse of a binary representation of a number is",s)
print("enter a number")
x=int(input())
bina(x)  
