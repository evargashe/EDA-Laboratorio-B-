import numpy as np
from matplotlib import pyplot as plt

#t,a = np.loadtxt('BubbleSort/valores_C++.txt',delimiter = ',',unpack = True)
t,a = np.loadtxt('../C/tiempos/heapsort_tiempo_c++.txt',delimiter = ',',unpack = True)
x,y = np.loadtxt('../Python/tiempos/heapsort_tiempo_python.txt',delimiter = ',',unpack = True)
m,n = np.loadtxt('../Java/tiempos/heapsort_tiempo_java.txt',delimiter = ',',unpack = True)
plt.plot(t,a, color = "blue",label = "C++")
plt.plot(x,y, color = "red",label = "Python")
plt.plot(m,n, color = "green",label = "Java")
plt.title('HeapSort Comparacion C++ Java Python')
plt.xlabel('# elementos')
plt.ylabel('tiempo-segundos')
plt.legend()
plt.show()
