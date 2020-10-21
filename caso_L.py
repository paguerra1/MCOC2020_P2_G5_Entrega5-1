from reticulado import Reticulado,data
from barra import Barra
from graficar3d import ver_reticulado_3d
from math import *
import numpy as np 

puntos = data()

def caso_L():
        
    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 
    
    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N
    
    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa
    
    #parámetros 
    A = 10.0*m**2

    q = 400*kg/m**2
    #Inicializar modelo
    ret = Reticulado()
    
    #Nodos
    
    #nodos 0-5 (6 nodos en total)
    for i in range(10,15,2):
        ret.agregar_nodo(puntos[i],0,puntos[i+1])
        ret.agregar_nodo(puntos[i],2,puntos[i+1])
        
    #nodos barras tablero 6-89 (86 nodos en total)
    for i in range(15,221,5):
        ret.agregar_nodo(i,0,100)
        ret.agregar_nodo(i,2,100)
    
    #nodos 90-95 (6 nodos en total)
    for i in range(56,62,2):
        ret.agregar_nodo(puntos[i],0,puntos[i+1])
        ret.agregar_nodo(puntos[i],2,puntos[i+1])
        
    #nodos 96 x 142
    for i in np.arange(2.5,235,5):
        ret.agregar_nodo(i,1,102.88)

    #Barras
    
    props = [8*cm, 5*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
    props2 = [12*cm, 15*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
    props3 = [13*cm, 15*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
    for i in range(0,94):
        ret.agregar_barra(Barra(i,i+2,*props2)) #eje x
    for i in range(0,95,2):
        ret.agregar_barra(Barra(i,i+1,*props3)) #eje y
    for i in range(96,142):
        ret.agregar_barra(Barra(i,i+1,*props))
        
    j=0 #union triangular
    for i in range(96,143):
            ret.agregar_barra(Barra(i,j,*props))
            ret.agregar_barra(Barra(i,j+1,*props))
            ret.agregar_barra(Barra(i,j+2,*props))
            ret.agregar_barra(Barra(i,j+3,*props))
            j+=2
    
    #Restricciones
    ret.agregar_restriccion(0,0,0)
    ret.agregar_restriccion(0,1,0)
    
    ret.agregar_restriccion(1,0,0)
    ret.agregar_restriccion(1,1,0)
    
    ret.agregar_restriccion(94,1,0)
    ret.agregar_restriccion(95,1,0)
    
    #Fuerzas
    for i in range(0,96):
        ret.agregar_fuerza(i,2,q*A)
    return ret
