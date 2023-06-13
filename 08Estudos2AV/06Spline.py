import matplotlib.pyplot as plt
import numpy as np

def splineLinear(xi, xiant, fxi, fxiant, x):
  si = (fxiant*(xi-x)/(xi-xiant)) + (fxi*(x-xiant)/(xi-xiant))
  return si

def SLM(xi,xiant,fxi,fxiant,t):
  yt = []
  for i in t:
    yt.append(splineLinear(xi,xiant,fxi,fxiant,i))
  return yt


x  = [1, 2, 5, 7]
fx = [1, 2, 3, 2.5]

t1 = np.linspace(1,2,10)
s1 = SLM(x[1],x[0],fx[1],fx[0],t1)
t2 = np.linspace(2,5,10)
s2 = SLM(x[2],x[1],fx[2],fx[1],t2)
t3 = np.linspace(5,7,10)
s3 = SLM(x[3],x[2],fx[3],fx[2],t3)

plt.plot(t1,s1,'b-')
plt.plot(t2,s2,'r-')
plt.plot(t3,s3,'g-')
plt.grid()
plt.plot()