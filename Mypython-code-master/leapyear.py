year=int(input("enter a year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year",year)
        else:
            print("not a leap year")
    else:
        print("leap year",year)
else:
    print("not a leap year",year)
 