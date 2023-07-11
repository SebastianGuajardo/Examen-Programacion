#programa principal
import os
import numpy as np 
import Funciones_Examen as fa 
Departamento=np.empty([4,10],type(int))
tipo=np.empty([4,10],type(int))
ruts=[]
fa.llenar(Departamento,tipo)
op=0
DepartamentoDisponible=0
suma=0
while(op!=5):
    os.system("cls")
    print("     Casa Feliz    ")
    print(" [1]  Comprar departamento ")
    print(" [2]  Mostrar departamentos disponibles ")
    print(" [3]  Ver listado de compradores ")
    print(" [4]  Mostrar ganancias totales ")
    print(" [5]  Salir ")
    op=fa.validarOP()
    if(op==2):
        fa.mostrarDisponibles(Departamento)
        os.system("pause")
    if(op==1):
        dd=fa.DepaDispo()
        fa.mostrarDisponibles(Departamento)
        DepartamentoDisponible=fa.validaDepa()
        cc=fa.disponible(Departamento,DepartamentoDisponible)
        if (cc): 
            print("*** Departamento Disponible ***")
            pagar=fa.comprarDepa(Departamento,DepartamentoDisponible,dd, tipo,ruts )
            print("\t Usted deberá cancelar un total de: $", pagar)
            os.system("pause")
    if(op==4):
        suma=0
        suma=fa.DepartamentoVendido(tipo)
        if(suma==0):
            print(" No se han vendido Departamentos aún")
        else:
            print(" El total vendido hasta ahora es de : $", suma)
        os.system("pause")
    if(op==3):
        fa.Listado(ruts)
        os.system("pause")
    if(op==5):
        print("----Adios----, Sebastian Guajardo, Fecha: 11/07/2023")
        












