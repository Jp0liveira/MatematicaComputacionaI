import numpy as np
import math

def f(x):
  d = {0.0:1.5, 0.5:2.0, 1.0:2.0, 1.5: 1.6364, 2.0:1.25, 2.5:0.9565 }
  y = d[x]
  return y

def trapezio(x):
  h = x[1] - x[0]
  b = (f(x[0])+f(x[1]))/2
  y = b*h
  return y

def trapezioR(x):
  n = len(x)
  h = x[1] - x[0]
  soma = (f(x[0])+f(x[n-1]))
  for e in x[1:n-1]:
    soma = soma + 2*f(e)

  y = soma*h/2
  return y

def simpsonR(x):
  n = len(x)
  h = x[1] - x[0]
  soma = (f(x[0])+f(x[n-1]))
  for i in range(1,n-1):
    if (i % 2 == 1):
      soma = soma + 4*f(x[i])
    else:
      soma = soma + 2*f(x[i])

  y = soma*h/3
  return y


x = [0, 2.5]
print("It = ",trapezio(x))
x = np.arange(0,2.6,0.5)
print("Itr = ",trapezioR(x))
x = np.arange(0,2.1,0.5)
I1 = simpsonR(x)
x = [2.0, 2.5]
I2 = trapezio(x)
print("I1 = ",I1,"I2 = ",I2,"IT = ",I1+I2)