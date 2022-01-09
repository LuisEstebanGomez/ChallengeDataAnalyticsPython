import csv
import requests
import os
from datetime import date
from datetime import datetime
import time



def download_files():

        """
        La funcion descarga los tres archivos de distintas fuentes y crea los directorios correspondientes 
        """

        #URL DE LAS FUENTES DE ARCHIVOS
        url_museos = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv'
        url_salas_cine = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
        url_bibliotecas_populares = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'   

        download = requests.get(url_museos)
        download_1 = requests.get(url_salas_cine)
        download_2 = requests.get(url_bibliotecas_populares)

        content = download.content
        content_1 = download_1.content
        content_2 = download_2.content

        #FECHA PARA CONTACETENAR AL NOMBRE DEL ARCHIVO
        fecha_arch= datetime.today().strftime('%d-%m-%Y')

        #FECHA PARA EL NOMBRE DEL DIRECTORIO DONDE ESTARA EL ARCHIVO
        directory = datetime.today().strftime('%Y-%B')

        
        #CREO LOS NOMBRES DE LOS DIRECTORIOS Y CREO LOS DIRECTORIOS
        File_Path = os.getcwd() + "\\datos" + "\\museos\\" + directory + "\\"  
        File_Path_1 = os.getcwd() + "\\datos" + "\\salas_cine\\" + directory + "\\"  
        File_Path_2 = os.getcwd() + "\\datos" + "\\bibliotecas_populares\\" + directory + "\\"  

        os.makedirs (File_Path)    
        os.makedirs (File_Path_1) 
        os.makedirs (File_Path_2)      
        
        #CREO ARCHIVO MUSEOS
        file = open(os.getcwd() + "\\datos\\museos\\" + directory + "\\museos-" + fecha_arch + ".csv" , 'wb')
        file.write(content)
        file.close()     

        #CREO ARCHIVO CINES
        file_1 = open(os.getcwd() + "\\datos\\salas_cine\\" + directory + "\\salas_cine-" + fecha_arch + ".csv" , 'wb')
        file_1.write(content)
        file_1.close()      

        #CREO ARCHIVO BIBLIOTECAS
        file_2 = open(os.getcwd() + "\\datos\\bibliotecas_populares\\" + directory + "\\bibliotecas_populares-" + fecha_arch + ".csv" , 'wb')
        file_2.write(content)
        file_2.close()      

