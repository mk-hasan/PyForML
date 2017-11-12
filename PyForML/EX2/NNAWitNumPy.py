import data 

import numpy as np

def pydistance(x1,x2):
    return sum([(x1d-x2d)**2 for x1d,x2d in zip(x1,x2)])

def pynearest(u,X,Y,distance=pydistance):
    xbest= None
    ybest= None
    dbest=float('inf')
    
    
    for x,y in zip(X,Y):
        d = distance(u,x)
        if d<dbest:
            ybest=y
            xbest=x 
            dbest = d 
    return ybest 

def pybatch(U,X,Y,nearest=pynearest,distance=pydistance):
    return [nearest(u,X,Y,distance=distance) for u in U]


U,X,Y = data.toy(20,100,50)
print (pybatch(U,X,Y))

#making new distance with numpy instead of loop

def npdistance(x1,x2):
    x1=np.array(x1)
    x2=np.array(x2)
    return np.sum((x1-x2)**2)

U,X,Y = data.toy(20,100,50)

batch_num = pybatch(U,X,Y,distance=npdistance)
batch_py = pybatch(U,X,Y)
print "Result are equal??"

print batch_num == batch_py

#calculating new nearest with numpy instead of for loop

def npnearest(u,X,Y,distance=npdistance):
    X=np.array(X)
    Y=np.array(Y)
    u=np.array(u)
    ind = np.argmin(np.sum((u-X)**2,axis=1))
    return Y[ind]

U,X,Y= data.toy(20,100,50)
batch_num= pybatch(U,X,Y,nearest=npnearest)
batch_py= pybatch(U,X,Y)
print "Results are equal?"
print batch_num == batch_py


#calculating new npbatch with numpy instead of pybatch

def npbatch(U,X,Y):
    U = np.array(U)
    X = np.array(X)
    Y = np.array(Y)
    U = np.array(np.repeat(U[:,:,None],X.shape[0],axis=2))
    X = np.array(np.repeat(X[:,:,None],U.shape[0],axis=2))
    X = X.swapaxes(0,2)
    S = np.sum((U-X)**2,axis=1)
    M = S.argmin(1)
    return Y[M]

U,X,Y = data.toy(20,100,50)
batch_num = npbatch(U,X,Y)
print 'Results are equal?'
print  batch_num == batch_py
