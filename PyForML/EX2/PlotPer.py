import matplotlib
from matplotlib import pyplot as plt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf','png')
plt.rcParams['savefig.dpi'] = 90
import time 
import data
import NNAWitNumPy

#Values for the number of dimensions d to test
dlist  = [1,2,5,10,20,50,100]

#Measure the computation time for each choice of number of dimensions d

tlist = []
for d in dlist:
    U,X,Y= data.toy(100,100,d)
    a=time.clock();
    NNAWitNumPy.pybatch(U,X,Y)
    b=time.clock()
    tlist = tlist+[b-a]

#plot the results in a graph
plt.figure(figsize=(5,3))
plt.plot(dlist,tlist,'-o')
plt.xscale('log');plt.yscale('log');plt.xlabel('d');plt.ylabel('time');plt.grid(True)



#Testing the performance of pybatch with pydistance and npdistance method

dlist2=[1,2,5,10,20,50,100,200,500,1000]

tlist1 =[]
tlist2=[]

for d in dlist2:
    U,X,Y = data.toy(100,100,d)
    a = time.clock()
    pybatch(U,X,Y)
    b=time.clock()
    pybatch(U,X,Y,distance=npdistance)
    
    c=time.clock()
    tlist1+=[b-a]
    tlist2+=[c-b]
    
#plot the result in a graph

plt.figure(figsize=(5,3))
plt.plot(dlist2,tlist1,'-o',label='normal')
plt.plot(dlist2,tlist2,'-o',label='npdistance')
plt.legend(loc='upper left')
plt.xscale('log');plt.yscale('log');plt.xlabel('d');plt.ylabel('time');plt.grid(True)
