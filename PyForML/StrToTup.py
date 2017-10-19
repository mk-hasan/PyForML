def StrToTup(x):
    data=[]
    for line in x:
        L=str.split(line[:-1],',')
        L[1]=int(L[1])
        data=data+[tuple(L)]
    print data

f=open("health-test.txt",'r')
StrToTup(f)