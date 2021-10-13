import os
import subprocess
hashOriginal=input("Inserta el hash verdadero:")
pwd=os.getcwd()
print(pwd)
for f in os.listdir("imagenes"):
    output= subprocess.Popen(["md5sum " + pwd + "/imagenes/"+f], stdout=subprocess.PIPE, shell=True)
    output=output.stdout.read().decode("utf-8")
    hash=output.split()
    if hashOriginal == (hash[0]):
            print ("La imagen que buscas es " + f)
            break
