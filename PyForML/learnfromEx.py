def LFX(x):
    tuple_set = []
    for line in x:
        L = str.split(line[:-1],',')
        L[1]= int(L[1])
        tuple_set = tuple_set + [(tuple(L[:3]),L[3])]
    print tuple_set
    
f=open('/home/mk/PyML/health-train.txt','r')
LFX(f)
   