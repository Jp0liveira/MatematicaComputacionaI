import numpy as np
import math

def f(x):
  y = np.exp(x)
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


x = [0, 1]
print("It = ",trapezio(x))
x = np.arange(0,1.1,0.1)
print("Itr = ",trapezioR(x))
prec = float(input('Entre com a precisão: '))
maximo = max(f(x))
h = (12*prec/maximo)**(0.5)
n = 1/h
print("Número de subintervalos: ",math.ceil(n))