import numpy as np
from matplotlib import pyplot as plt

"""
a,b = np.loadtxt('BubbleSort/valores_C++.txt',delimiter = ',',unpack = True)
c,d = np.loadtxt('CountingSort/valores_C++.txt',delimiter = ',',unpack = True)
e,f = np.loadtxt('HeapSort/valores_C++.txt',delimiter = ',',unpack = True)
g,h = np.loadtxt('InsertionSort/valores_C++.txt',delimiter = ',',unpack = True)
i,j = np.loadtxt('MergeSort/valores_C++.txt',delimiter = ',',unpack = True)
k,l = np.loadtxt('Quicksort/valores_C++.txt',delimiter = ',',unpack = True)
m,n = np.loadtxt('SelectionSort/valores_C++.txt',delimiter = ',',unpack = True)
"""
a,b = np.loadtxt('../Python/tiempos/burbuja_tiempo_python.txt',delimiter = ',',unpack = True)
c,d = np.loadtxt('../Python/tiempos/heapsort_tiempo_python.txt',delimiter = ',',unpack = True)
e,f = np.loadtxt('../Python/tiempos/insertionsort_tiempo_python.txt',delimiter = ',',unpack = True)
g,h = np.loadtxt('../Python/tiempos/mergesort_tiempo_python.txt',delimiter = ',',unpack = True)
i,j = np.loadtxt('../Python/tiempos/quicksort_tiempo_python.txt',delimiter = ',',unpack = True)
k,l = np.loadtxt('../Python/tiempos/selectionsort_tiempo_python.txt',delimiter = ',',unpack = True)
m,n = np.loadtxt('../Python/tiempos/shellsort_tiempo_python.txt',delimiter = ',',unpack = True)

plt.plot(a,b, color = "blue",label = "BubbleSort")
plt.plot(c,d, color = "red",label = "HeapSort")
plt.plot(e,f, color = "green",label = "InsertionSort")
plt.plot(g,h, color = "cyan",label = "MergeSort")
plt.plot(i,j, color = "yellow",label = "QuickSort")
plt.plot(k,l, color = "black",label = "SelectionSort")
plt.plot(m,n, color = "magenta",label = "ShellSort")
plt.title('Algoritmos Ordenamiento Python')
plt.xlabel('# elementos')
plt.ylabel('tiempo-segundos')
plt.legend()
plt.show()
