from random import randint

def generador(f,tam):
    while tam>0:
        a=randint(0,9)
        f.write(str(a) + "\n")
        tam=tam-1

""" def copia(a,f,tam):
    linea=f.line(0)
    while  """

f=open("generador.txt",'w')
generador(f,100000)





