import numpy as np
import pandas as pd
from random import seed
from random import random
import matplotlib.pyplot as plt
P = np.array([[0.2, 0.7, 0.1],
              [0.9, 0.0, 0.1],
              [0.2, 0.8, 0.0]])
state=np.array([[1.0, 0.0, 0.0]])
stateHist=state
dfStateHist=pd.DataFrame(state)
distr_hist = [[0,0,0]]
for x in range(50):
  state=np.dot(state,P)
  print(state)
  stateHist=np.append(stateHist,state,axis=0)
  dfDistrHist = pd.DataFrame(stateHist)
  dfDistrHist.plot()
plt.show()

def add(a,b,c):
    return a+b+c

def test_unity():
    assert add(state[:2])==1
    

#%%
I = np.identity(3)
A=np.append(P.transpose()-I,[[1,1,1]],axis=0)
b=np.array([0,0,0,1])
b_T=b.transpose()
np.linalg.solve(A.transpose().dot(A), A.transpose().dot(b_T))

