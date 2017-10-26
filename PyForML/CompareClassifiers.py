import NearestNeighbourClasifier

def DtoDTree(x):
    decision=''
    counter=0
    if(x[0]=='yes'):
        if x[1]>29.5:
            decision='more'
                
        else:
            decision='less'
    elif x[0]=='no':
        if x[2]=='good':
            decision = 'less'
        elif x[2]=='poor':
            decision='more'
    else:
        decision='others'
    return decision

def findUncommonTuples(x):
    uncommon_tuples=[]
    for element in x:
        classifier1= DtoDTree(element)
        print classifier1
        classifier2= NearestNeighbourClasifier.NearestNeighAlgo(element,NearestNeighbourClasifier.t_set)
        if classifier1!=classifier2:
            uncommon_tuples += [element]
    uncommon_tuples_rate= float(len(uncommon_tuples))/len(NearestNeighbourClasifier.t_set)
    print uncommon_tuples_rate , uncommon_tuples