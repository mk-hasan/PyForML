def tuple_set1(x):
    tuple_set = []
    for line in x:
        L = str.split(line[:-1],',')
        L[1]= int(L[1])
        tuple_set = tuple_set + [(tuple(L[:3]),L[3])]
    return tuple_set


def d(a,b):
    return (a[0]!=b[0])+((a[1]-b[1])/50.0)**2+(a[2]!=b[2])

def NearestNeighAlgo(test_tuple,t_set):
    distance = d(test_tuple,t_set[0][0])
    index = 0
    for element in t_set[1:]:
        if d(test_tuple,element[0]) < distance:
            distance = d(test_tuple,element[0])
            index = t_set.index(element)
    return test_tuple,t_set[index][1]


    
f=open('/home/mk/PyML/health-train.txt','r')
t_set= tuple_set1(f)
test_tuple=('yes',31,'good')
NNResult = NearestNeighAlgo(test_tuple,t_set)
print NNResult
        
    