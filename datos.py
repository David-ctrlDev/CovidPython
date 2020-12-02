import mysql.connector
from registros import * 
from censo import * 

#Visualizamos los datos de los pacientes censados
def visualizarDatos():
    print("")
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd= "", db='Censo' )
    cur = miConexion.cursor()
    print("PACIENTES CENSADOS"+"\n" 
    + "--------------------------------------")
    cur.execute(" SELECT paciente.nro_Cedula, paciente.nombre_y_Apellido,\
                enfermedad.nombre_enfermedad from paciente\
                inner join paciente_enfermedad on paciente.nro_cedula = paciente_enfermedad.nro_cedula\
                inner join enfermedad on enfermedad.IDenfermedad = paciente_enfermedad.IDenfermedad")
    for nro_Cedula, nombre_y_Apellido, nombre_enfermedad in cur.fetchall():
            print("Paciente:  " + nro_Cedula + ", ", nombre_y_Apellido + ","  , nombre_enfermedad)
       
#Visualizamos los pacientes en alto riesgo por presentar dos enfermedades o más
def visualizarDatos2():
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd= "", db='Censo' )
    cur = miConexion.cursor()
    print( "PACIENTES EN ALTO RIESGO" +"\n" 
    + "--------------------------------------")
    cur.execute("SELECT paciente.nro_Cedula, paciente.nombre_y_Apellido\
                 from paciente inner join paciente_enfermedad on\
                      paciente.nro_cedula = paciente_enfermedad.nro_cedula\
                      inner join enfermedad on enfermedad.IDenfermedad = paciente_enfermedad.IDenfermedad\
                      GROUP BY nro_Cedula HAVING COUNT(*)>1")
    for nro_Cedula, nombre_y_Apellido in cur.fetchall():
            print("Paciente:  " + nro_Cedula + ",",  nombre_y_Apellido)
#Visualizamos que paciente sufre que enfermedad
def visualizarDatos3():
    print("PACIENTES CATALOGADOS POR ENFERMEDAD")
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd= "", db='Censo' )
    cur = miConexion.cursor()
    enfermedad = input("Qué enfermedad sufren los pacientes que buscas?: ")
    cur.execute(" SELECT paciente.nro_Cedula, paciente.nombre_y_Apellido,\
                enfermedad.nombre_enfermedad from paciente\
                inner join paciente_enfermedad on paciente.nro_cedula = paciente_enfermedad.nro_cedula\
                inner join enfermedad on enfermedad.IDenfermedad = paciente_enfermedad.IDenfermedad")
    for nro_Cedula, nombre_y_Apellido, nombre_enfermedad in cur.fetchall():
            if enfermedad == nombre_enfermedad:
                print("Paciente:  " + nro_Cedula + ", ", nombre_y_Apellido + ","  , nombre_enfermedad)
#Visualizamos sospechosos de portar el virus, por sufrir todos los sintomas
def visualizarDatos4():
    print("POSIBLES PORTADORES DE COVID19" +  "\n" 
    + "--------------------------------------")
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd= "", db='Censo' )
    cur = miConexion.cursor()
    cur.execute("SELECT paciente.nro_Cedula, paciente.nombre_y_Apellido\
                 from paciente inner join paciente_sintoma on\
                      paciente.nro_cedula = paciente_sintoma.nro_cedula\
                      inner join sintoma on sintoma.IDsintoma = paciente_sintoma.IDsintoma\
                      GROUP BY nro_Cedula HAVING COUNT(*)>4")
    for nro_Cedula, nombre_y_Apellido in cur.fetchall():
            print("Paciente:  " + nro_Cedula + ",",  nombre_y_Apellido)
#Visualizamos Frecuencias Absolutas
def visualizarDatos5():
    print( "FRECUENCIA ABSOLUTA x ENFERMEDAD" +"\n" 
    + "--------------------------------------")
    enfermedad = input("Enfermedad de la que desees ver la frecuencia: (Solo el ID) ")
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd= "", db='Censo' )
    cur = miConexion.cursor()
    cur.execute("SELECT nro_Cedula, IDenfermedad from paciente_enfermedad")
    frecuenciaAbsoluta = 0
    for nro_Cedula, IDEnfermedad in cur.fetchall():
        
        if IDEnfermedad == enfermedad:
            frecuenciaAbsoluta =+1
    print(" La frecuencia absoluta para la enfermedad " + enfermedad + ": " +"es = " +str(frecuenciaAbsoluta))
#Visualizamos promedio de edad de los censados
def visualizarDatos6():
    print("PROMEDIO EDAD" +"\n" 
    + "--------------------------------------")
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd= "", db='Censo' )
    cur = miConexion.cursor()
    sumaEdades = 0
    cur.execute("SELECT AVG(TIMESTAMPDIFF(YEAR, nacimiento, CURDATE()))\
                 AS `Average` from paciente WHERE nacimiento IS NOT NULL")
    for AVG in cur.fetchall():
        promedio = list(AVG)
        print((promedio[0]), "Años")
    


            

    

    
