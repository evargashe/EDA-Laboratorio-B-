import abc
from time import time
from random import randint

def lectura(x,k):
    f=open("../generador.txt",'w')
    for i in range(k):
        a=randint(1,9)
        f.write(str(a))
    f.close()


    archivo = open("../generador.txt","r")
    avance = 0
    linea=archivo.read(1)
    while linea!="":
        x.append(int(str(linea)))
        linea=archivo.read(1)
    archivo.close()



def partition(a,low,high):
    i = ( low-1 )
    pivot = a[high]
    for j in range(low , high):
        if a[j] < pivot:
            i = i+1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[high] = a[high],a[i+1]
    return ( i+1 )
def quickSort(a,low,high):
    if low < high:
        pi = partition(a,low,high)
        quickSort(a, low, pi-1)
        quickSort(a, pi+1, high)


def set_data(tamanho,tiempo):
  helper.write(str(tamanho) + " , "+ str(tiempo) + "\n")


a = []


helper = open("./tiempos/quicksort_tiempo_python.txt","w")

for k in range(1,21):
    n=500*k
    lectura(a,n)
    start_time = time()
    quickSort(a,0,len(a)-1)
    elapsed_time = time() - start_time
    set_data(len(a),round(float(elapsed_time),4))
    del a[:]

helper.close()