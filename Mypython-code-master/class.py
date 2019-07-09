y=10
print("outside function",y)
def f1():
    global y
    y=5 ;
    print("inside function",y)
f1()
print("outside function",y)
