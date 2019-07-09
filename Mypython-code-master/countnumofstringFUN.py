def stri(s):
    words=1;
    for x in s:
        if(x==' '):
            words=words+1
    return words
st=input()
print("number of words is",stri(st))
        
