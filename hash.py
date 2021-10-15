import os
import subprocess
hashOriginal=input("Inserta el hash verdadero:")
pwd=os.getcwd()
print(pwd)
for f in os.listdir("imagenes"): #debes escribir el nombre de la carpeta de los archivos a analizar
    output= subprocess.Popen(["md5sum " + pwd + "/imagenes/"+f], stdout=subprocess.PIPE, shell=True) #debes cambiar el directorio donde estan los archivos
    output=output.stdout.read().decode("utf-8")
    hash=output.split()
    if hashOriginal == (hash[0]):
            print ("El archivo que buscas es " + f)
            break
