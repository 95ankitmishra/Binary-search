x=int(input("enter a number"))
y=int(input("enter another number"))
try:
    z=x/y
    print("division result",z)
except ZeroDivisionError:
    print("please preess greater than zero int values")
finally:
    print("in final")
    print("hello this is last line")
