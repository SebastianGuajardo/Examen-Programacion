
import os
import numpy as np 
def llenar(mm,tipo): 
    p=1
    for i in range(4):
        for j in range(10):
            mm[i,j]=p 
            tipo[i,j]=p 
            p+=1 
def validarOP():
    pp=0
    while(True):
        try:
            pp=int(input("   Elija opción: "))
            if(pp>=1 and pp<=5):
                break
            else:
                print("Debe ingresar una opción entre 1 y 5")
        except ValueError:
            print("Debe ingresar un número entero")
    return pp 
def mostrarDisponibles(Departamento):
    os.system("cls")
    for i in range(4):
        print("\n") 
        for j in range(10):
            if(j==1 or j==5):
                print("\t",Departamento[i,j], end="        ")
            else:
                print("\t",Departamento[i,j], end="   ")
    print("\n\n")
def DepaDispo():
    os.system("cls")
    des=""
    while(len(des)<=0):
        print("Departamento Tipo A")
        print("Departamento Tipo B")
        print("Departamento Tipo C")
        print("Departamento Tipo D")
        des=input("   Elija Departamento: ").lower()
        if(des!="Tipo A" and des!="Tipo B" and des!="Tipo C" and des!="Tipo D"):
            print("Debe ingresar una opcion correcta")
            des=""
    return des 
def validaDepa():
    asiento=0
    while(True):
        try:
            DepartamentoDisponible=int(input(" Ingrese Departamento entre 1 a 40: "))
            if(asiento>=1 and DepartamentoDisponible<=10):
                break
            else:
                print("Error debe ingresar un departamento entre 1 a 40")
        except ValueError:
            print("Debe ser un número entero")
    return asiento 
def disponible(Departamento,DepartamentoDisponible):
    for i in range(10):
        for j in range(4):
            if(DepartamentoDisponible==Departamento[i,j]):
                return True
    return False
def comprarDepa(aa,asiento,dd, otra,ruts):
    if(dd=="Tipo A"):
        pago=137163432
    if(dd=="Tipo B"):
        pago=108286920
    if(dd=="Tipo C"):
        pago=101067792
    if(dd=="Tipo D"):
        pago=126334740
    for i in range(4):
        for j in range(10):
            if(asiento==aa[i,j]):
                while(True):
                    while(True):
                        try:
                            rut=int(input("Rut debe tener 8 digitos minimo "))
                            if(rut<9999999):
                                print("Error, debe tener 8 dígitos mínimo")
                            else:
                                break
                        except ValueError:
                            print("Debe ser número entero")
                    if(len(ruts)>0): 
                        pr=0
                        for y in range(len(ruts)):
                            if(rut==ruts[y]):
                                pr=1
                        if(pr==1):
                            print("Departamento Vendido, **NO ESTA DISPONIBLE** ")
                        else:
                            ruts.append(rut)
                            break
                    else:
                        ruts.append(rut)
                        break
                aa[i,j]="X" 
            

def DepartamentoVendido(aa):
    suma=0
    for i in range(4):
        for j in range(10):
            if(aa[i,j]!=1 and aa[i,j]>40):
                suma+=aa[i,j]
    return suma
def Listado(r):
    r.sort()
    print("Listado De compradores ordenados de menor a mayor ")
    print("\t",r)













