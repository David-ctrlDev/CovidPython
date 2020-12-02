import mysql.connector
from registros import *
from datos import *
import os

#=============================

#funciones de menu

def mostarMenuPrincipal():
    
    print('CENSO POBLACIONAL DE RIESGOS POR COVID19')
    print('===============================')
    print('(1) Registrar nuevo paciente')
    print('(2) Registrar Enfermedades ')
    print('(3) Registrar Sintomas')
    print('(4) Ver Datos')
    print('')
    print('(0) Terminar')
    print('')
    opcion = int(input('Cual opcion?" '))
    return opcion
    
def mostarMenuSecundario():
    
    print('DATOS RELEVANTES PARA LAS ESTADISTICAS')
    print('===============================')
    print('(1) Visualizar pacientes censado')
    print('(2) Visualizar pacientes con mayor riesgo ')
    print('(3) Pacientes según (x) Enfermedad')
    print('(4) Visualizar posibles portadores de COVID19')
    print('(5) Visualizar Frecuencias Absolutas')
    print('(6) Visualizar Promedio de edad de censados')
    print('(7) Regresar al menú principal')
    print('')
    print('(0) Terminar')
    print('')
    opcion = int(input('Cual opcion?" '))
    return opcion

def ejecutarMenu():

    
    opcion = mostarMenuPrincipal()
    while opcion > 0:
        if opcion == 1:
            crearRegistro()
        if opcion == 2:
            registrarEnfermedades()
        if opcion == 3:
            registrarSintomas()
        if opcion == 4:
            ejecutarMenuSecundario()
        os.system("pause")
        opcion = mostarMenuPrincipal()
        
    print('Hast pronto!')

def ejecutarMenuSecundario():
    
    
    opcion = mostarMenuSecundario()
    while opcion > 0:
        if opcion == 1:
            visualizarDatos()
        if opcion == 2:
            visualizarDatos2()
        if opcion == 3:
            visualizarDatos3()
        if opcion == 4:
            visualizarDatos4()
        if opcion == 5:
            visualizarDatos5()
        if opcion == 6:
            visualizarDatos6()
        os.system("pause")
        if opcion == 7:
            ejecutarMenu()
        opcion = mostarMenuSecundario()
        
    print('Hast pronto!')


if __name__ == '__main__':
   ejecutarMenu()