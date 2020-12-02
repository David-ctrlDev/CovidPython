import mysql.connector
def crearRegistro():
    tipo_documento = input('Tipo de documento: ')
    nombre_y_Apellido = input('Nombre y Apellidos: ')
    genero = input('Genero (M/F):  ')
    barrio = input("Barrio en el que vive actualmente: ")
    ciudad = input('Ciudad de residencia: ')
    telefono = input ("Número de telefono: ")
    nacimiento = input("Fecha de nacimiento( YYYY-MM-DD): " )
    profesion = input("Profesión: ")
    nacionalidad = input("Nacionalidad: ")
    nro_Cedula = input("Número de documento: ")
    insertar(tipo_documento, nombre_y_Apellido, genero, barrio, ciudad, telefono, nacimiento, profesion, nacionalidad, nro_Cedula)

#Ingresamos registros a la tabla Paciente
def insertar(tipo_documento, nombre_y_Apellido, genero, barrio, ciudad, telefono, nacimiento, profesion, nacionalidad, nro_Cedula):
    
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd= "", db='Censo' )
        cur = miConexion.cursor()
        sentenciaSQL = "INSERT INTO PACIENTE(tipo_documento, nombre_y_Apellido, genero, barrio, ciudad, telefono, nacimiento, profesion, nacionalidad, nro_Cedula) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)"
        cur.execute(sentenciaSQL, [tipo_documento, nombre_y_Apellido, genero, barrio, ciudad, telefono, nacimiento, profesion, nacionalidad, nro_Cedula])
        miConexion.commit() 
        
        print("Operacion realizada")

#Listamos la lista de enfermedades y hacemos la relacion Paciente_Enfermedad
def registrarEnfermedades():
    
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd= "", db='Censo' )
        cur = miConexion.cursor()
        cur.execute( "SELECT IDEnfermedad,Nombre_Enfermedad  FROM Enfermedad" )
        for IDEnfermedad, Nombre_enfermedad in cur.fetchall():
            print("ID : " +IDEnfermedad,"Nombre: " +Nombre_enfermedad)
        sentenciaSQL = "INSERT INTO PACIENTE_ENFERMEDAD(Nro_cedula, IDENfermedad ) VALUES (%s, %s)"
        NroDoc = input("Cedula del censado: ")
        respuesta = input("Deseas registrar una enfermedad?: (S)i | (N)o ")
        while respuesta == "S" or respuesta == "s":
            enfermedad = input("Ha sufrido o sufre alguna de las siguientes enfermedades? NOTA:(Ingrese sólo el ID)   Cual ó Cuales : ")
            sentenciaSQL = "INSERT INTO PACIENTE_ENFERMEDAD(Nro_cedula, IDENfermedad ) VALUES (%s, %s)"
            cur.execute(sentenciaSQL, [NroDoc, enfermedad])
            respuesta = input("Deseas registrar una  enfermedad?: (S)i | (N)o : ")
        miConexion.commit()

#Listamos Sintoma, generamos los registros de Sintoma y Relacionamos Paciente_Sintoma
def registrarSintomas():
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd= "", db='Censo' )
        cur = miConexion.cursor()
        NroDoc = input("Cedula del censado: ")
        respuesta = input("Deseas registrar un  sintoma? : (S)i | (N)o ")
        while respuesta == "S" or respuesta == "s":
            cur.execute( "SELECT IDSintoma,DESCRIPCION FROM ListaSintomas" )
            for IDSintoma, Descripcion in cur.fetchall():
                print("ID : " +IDSintoma,"Nombre: " +Descripcion)
            sintoma = input("Has tenido alguno de los siguientes sintomas? NOTA:(Ingrese sólo el ID)   Cual ó Cuales : ")
            Fecha_registro = input("Fecha en que presentó el sintoma: (AAAA-MM-DD): ")
            sentenciaSQL = "INSERT INTO Sintoma(IDSintoma, Fecha_registro) VALUES (%s, %s)"
            cur.execute(sentenciaSQL, [sintoma, Fecha_registro])
            sentenciaSQL2 = " INSERT INTO PACIENTE_SINTOMA(Nro_cedula, IDSintoma) VALUES (%s, %s)"
            cur.execute(sentenciaSQL2,[NroDoc,sintoma])
            respuesta = input("Deseas registrar otro sintoma?: (S)i | (N)o : ")
        miConexion.commit()

        miConexion.close()

