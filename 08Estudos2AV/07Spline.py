from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

x  = np.linspace(0, 10, num = 11, endpoint=True)
y  = np.cos(-x**2/9.0)
f1 = interp1d(x,y,kind='linear')
f2 = interp1d(x,y,kind='quadratic')
f3 = interp1d(x,y,kind='cubic')

fig, axs = plt.subplots(5)
fig.suptitle('Gráficos de Splines')

xnew = np.arange(0, 10, 0.01)

axs[0].plot(x,y,'go')
axs[1].plot(x,y,'go',xnew,f1(xnew),'r-')
axs[2].plot(x,y,'go',xnew,f2(xnew),'m-')
axs[3].plot(x,y,'go',xnew,f3(xnew),'b-')