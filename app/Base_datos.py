import psycopg2
import pandas as pd
import os
from datetime import date
from datetime import datetime
import time

def base_datos():

        PSQL_HOST = "localhost"
        PSQL_PORT = "5432"
        PSQL_USER = "postgres"
        PSQL_PASS = "1234"
        PSQL_DB   = "postgres"  

        # conecction
        try:
            connection_address = """ host=%s port=%s user=%s password=%s dbname=%s """ % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
            connection = psycopg2.connect(connection_address)
            cursor = connection.cursor()
            print(" conexion con la base de datos")    
        except:
            print("Error en la conexion con la base de datos")    

        sql ='''CREATE TABLE GENERAL(
        cod_localidad INT,
        id_provincia INT,
        id_departamento INT,
        Categoria TEXT,
        Provincia TEXT,
        Localidad TEXT,
        nombre TEXT,
        domicilio TEXT,
        codigo_postal TEXT,
        numero_de_telefono TEXT,
        mail TEXT,
        web TEXT,
        fecha_carga TEXT
        )'''


        cursor.execute(sql)
        connection.commit()

        #FECHA PARA CONTACETENAR AL NOMBRE DEL ARCHIVO
        fecha_arch= datetime.today().strftime('%d-%m-%Y')

        #FECHA PARA EL NOMBRE DEL DIRECTORIO DONDE ESTARA EL ARCHIVO
        directory = datetime.today().strftime('%Y-%B')

        current_dir = os.path.dirname(os.path.realpath(__file__)) 
        filename = os.path.join(current_dir, "datos\\bibliotecas_populares\\" + directory + "\\bibliotecas_populares-" + fecha_arch + ".csv") 

        bibliotecas = pd.read_csv(".\\datos\\bibliotecas_populares\\" + directory + "\\bibliotecas_populares-" + fecha_arch + ".csv",

                                    encoding ='latin-1',
                                    )

        museos = pd.read_csv(".\\datos\\museos\\" + directory + "\\museos-" + fecha_arch +".csv",
                                    encoding ='latin-1',
                                    )

        cines = pd.read_csv(".\\datos\\salas_cine\\" + directory + "\\salas_cine-" + fecha_arch + ".csv",

                                    encoding ='latin-1',
                                    )


        # para completar tabla general con todos los datos                        
        for row_index, row in bibliotecas.iterrows():
            
            sql1="INSERT INTO GENERAL(cod_localidad, id_provincia , id_departamento, Categoria, Provincia, Localidad, nombre, domicilio, codigo_postal, numero_de_telefono, mail, web, fecha_carga) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            datos=( row['localidad_id'],
                    row['provincia_id'],
                    row['espacio_cultural_id'],
                    'Bibliotecas',
                    row['provincia'],
                    row['localidad'],
                    row['nombre'],
                    row['direccion'],
                    row['codigo_postal'],
                    row['telefono'],
                    row['mail'],
                    row['web'],
                    date.today())
            cursor.execute(sql1, datos)

        for row_index, row in museos.iterrows():
            
            sql2="INSERT INTO GENERAL(cod_localidad, id_provincia , id_departamento, Categoria, Provincia, Localidad, nombre, domicilio, codigo_postal, numero_de_telefono, mail, web, fecha_carga) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            datos=( row['localidad_id'],
                    row['provincia_id'],
                    row['espacio_cultural_id'],
                    'Museos',
                    row['provincia'],
                    row['localidad'],
                    row['nombre'],
                    row['direccion'],
                    row['codigo_postal'],
                    row['telefono'],
                    row['mail'],
                    row['web'],
                    date.today())
            cursor.execute(sql2, datos)

        for row_index, row in bibliotecas.iterrows():
            
            sql3="INSERT INTO GENERAL(cod_localidad, id_provincia , id_departamento, Categoria, Provincia, Localidad, nombre, domicilio, codigo_postal, numero_de_telefono, mail, web, fecha_carga) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            datos=( row['localidad_id'],
                    row['provincia_id'],
                    row['espacio_cultural_id'],
                    'Cines',
                    row['provincia'],
                    row['localidad'],
                    row['nombre'],
                    row['direccion'],
                    row['codigo_postal'],
                    row['telefono'],
                    row['mail'],
                    row['web'],
                    date.today())
            cursor.execute(sql3, datos)

        connection.commit()
        #Closing the connection
        connection.close()