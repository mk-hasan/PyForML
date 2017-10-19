class DataToDecisionTree:
    def DtoDTree(self,x):
        decision=''
        counter=0
        if(x[0]=='yes'):
            if x[1]>29.5:
                decision='more risk'
                
            else:
                decision='less risk'
        elif x[0]=='no':
            if x[2]=='good':
                decision = 'less risk'
            elif x[2]=='poor':
                decision='more risk'
        else:
            decision='others'
        return decision
    def StrToTup(self,x):
        data=[]
        for line in x:
            L=str.split(line[:-1],',')
            L[1]=int(L[1])
            data=data+[tuple(L)]
        return data
    
    f=open("health-test.txt",'r')
    tuples=StrToTup(f)
    print tuples
    total=0
    totaldata=0
    for t in tuples:
        if DtoDTree(t)=='more risk':
            total=total+1
            totaldata=totaldata+1
        else:
            totaldata=totaldata+1
    print total
    
    print totaldata