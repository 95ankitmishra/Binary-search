val=tuple(int(x) for x in input("Enter tuple elements").split(','))
val2=tuple(int(x) for x in input("Enter tuple elements").split(','))
print(set(val2).issubset(set(val)))
