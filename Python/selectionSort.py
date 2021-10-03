from time import time
def selectionSort(a):
    n=len(a)-1
    while n>=0:
        mayor=a[0]
        pos=0
        for i in range(1,n+1):
            if mayor< a[i]:
                mayor = a[i]
                pos=i
        a[pos],a[n]=a[n],a[pos]
        n=n-1

