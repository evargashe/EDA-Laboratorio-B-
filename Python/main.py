from insertionSort import insertionSort
from bubbleSort import bubbleSort
from heapSort import heapSort
from selectionSort import selectionSort
from shellSort import shellSort
from mergeSort import mergeSort
from random import randint
from time import time
import sys



def generador(tam):
    f=open("../generador.txt",'w')
    while tam>0:
        a=randint(0,9)
        f.write(str(a))
        tam=tam-1
    f.close()
    a=[]
    g=open("../generador.txt",'r')
    linea=g.read(1)
    while linea!="":    
        a.append(int(str(linea)))
        linea=g.read(1)
    g.close()

    return a

""" def set_data(tiempo):
    helper = open("valores_python.txt","a")
    helper.write(str(tiempo) + "\n")
    helper.close() """

""" GENERAR """


arr=[]
arr2=[]
""" burbuja = open("./tiempos/burbuja_tiempo_python.txt","w") """
""" heapsort = open("./tiempos/heapsort_tiempo_python.txt","w") """
""" insertionsort = open("./tiempos/insertionsort_tiempo_python.txt","w") """
""" selectionsort = open("./tiempos/selectionsort_tiempo_python.txt","w") """
shellsort = open("./tiempos/shellsort_tiempo_python.txt","w")
mergesort = open("./tiempos/mergesort_tiempo_python.txt","w")



""" quicksort = open("./tiempos/quicksort_tiempo_python.txt","w")
 """
""" for i in range(1,21):
    
    n=5000*i
    arr=generador(n)
    print(len(arr))

    arr2=arr
    start_time = time()
    bubbleSort(arr2)                 
    elapsed_time = time() - start_time
    burbuja.write(str(n) + "," + str(round(float(elapsed_time),4)) + "\n")
    
    del arr2[:]
    del arr[:]


burbuja.close() """


""" HEAPSORT """

""" for i in range(1,21):
    n=5000*i
    arr=generador(n)

    arr2=arr
    start_time = time()
    heapSort(arr2)                 
    elapsed_time = time() - start_time
    heapsort.write(str(n) + "," + str(round(float(elapsed_time),4)) + "\n")



    del arr2[:]
    del arr[:]

heapsort.close() """

""" INSERTIONSORT
 """

""" for i in range(1,21):
    
    n=5000*i
    arr=generador(n)


    arr2=arr
    start_time = time()
    insertionSort(arr2)                 
    elapsed_time = time() - start_time
    insertionsort.write(str(n) + "," + str(round(float(elapsed_time),4)) + "\n")

    del arr2[:]
    del arr[:]


insertionsort.close()
 """

""" SELECTIONSORT
 """
 
""" for i in range(1,21):
    
    n=5000*i
    
    arr=generador(n)

    arr2=arr
    start_time = time()
    selectionSort(arr2)                 
    elapsed_time = time() - start_time
    selectionsort.write(str(n) + "," + str(round(float(elapsed_time),4)) + "\n")


    del arr2[:]
    del arr[:]


selectionsort.close() """


""" SHELLSORT """

for i in range(1,21):
    
    n=5000*i
    arr=generador(n)


    arr2=arr
    start_time = time()
    shellSort(arr2)                 
    elapsed_time = time() - start_time
    shellsort.write(str(n) + "," + str(round(float(elapsed_time),4)) + "\n")





    del arr2[:]
    del arr[:]


shellsort.close() 


""" MERGESORT
 """
for i in range(1,21):
    
    n=5000*i
    arr=generador(n)


    arr2=arr
    start_time = time()
    mergeSort(arr2)                 
    elapsed_time = time() - start_time
    mergesort.write(str(n) + "," + str(round(float(elapsed_time),4)) + "\n")


    del arr2[:]
    del arr[:]


mergesort.close()

















