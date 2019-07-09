c=complex(input("enter a complex number"))
if c.real > c.imag:
    print("%d is greater" %(c.real))
elif c.real < c.imag:
    print("%d is greater" %(c.imag))
else:
    print("both are same")
