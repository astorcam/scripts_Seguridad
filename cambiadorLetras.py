import operator
text= input("Mete el texto cifrado: ")
text=text.lower()
letraV=0
while letraV!="stop":
    letraV= input("¿Que letra de tu texto deseas cambiar mi amor de mi vida de mi corazon?")
    letraN= input ("¿Porque letra te molaria cambiarla?")
    letraN=letraN.upper()
    text=text.replace(letraV,letraN)
    print(text)
