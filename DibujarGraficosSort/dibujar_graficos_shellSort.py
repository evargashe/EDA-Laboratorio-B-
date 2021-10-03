import numpy as np
from matplotlib import pyplot as plt

#t,a = np.loadtxt('BubbleSort/valores_C++.txt',delimiter = ',',unpack = True)
t,a = np.loadtxt('../C/tiempos/shellsort_tiempo_c++.txt',delimiter = ',',unpack = True)
x,y = np.loadtxt('../Python/tiempos/shellsort_tiempo_python.txt',delimiter = ',',unpack = True)
m,n = np.loadtxt('../Java/tiempos/shellsort_tiempo_java.txt',delimiter = ',',unpack = True)
plt.plot(t,a, color = "blue",label = "C++")
plt.plot(x,y, color = "red",label = "Python")
plt.plot(m,n, color = "green",label = "Java")
plt.title('ShellSort Comparacion C++ Java Python')
plt.xlabel('# elementos')
plt.ylabel('tiempo-segundos')
plt.legend()
plt.show()
