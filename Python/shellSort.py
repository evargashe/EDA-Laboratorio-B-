
def shellSort(a):
    n=len(a)
    intervalo=n//2

    while intervalo>0:
        j=intervalo
        for i in range(0,n):
            if(j<n):
                if a[i]>a[j]:
                    a[i],a[j]=a[j],a[i]
                    if(intervalo==1):   
                        key=a[i]
                        k=i-1
                        while k>=0 and key<a[k]:
                            a[k+1]=a[k]
                            k-=1
                        a[k+1]=key
            j+=1
        intervalo=intervalo//2


