chance=1
while chance <=9:
    x=int(input("enter a number"))
    if x%2==0:
        break
    chance=chance+1
    if chance==4:
        print("you lost")
        
    else:
        print("you win")
