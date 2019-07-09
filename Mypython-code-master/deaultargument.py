def f1(**k):
    print("person information")
    for key,value in k.items():
        print(key,"-",value)
name=input("enter a name")
age=input("Enter age")
percentage12th=float(input("enter percentage"))
salary=int(input("enter salary"))
f1(name,age,percentage12th,salary)

