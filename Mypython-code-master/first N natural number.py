def recnat(n):
    if n>0:
        recnat(n-1)
        print(n,end=" ")
