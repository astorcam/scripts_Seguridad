import operator

text= input("Mete el texto cifrado: ")
letras=["e","a","o","l","s","n","d","r","u","i","t","c","p","m","y","q","b","h","g","f","v","j","ñ","z","x","k","w"]
caracteres={}
for char in text:
	if char.isalpha() or char=="ñ":
		if char in caracteres:
			caracteres[char]+=1
		else:
			caracteres [char]=1

apariciones = dict( sorted(caracteres.items(), key=operator.itemgetter(1),reverse=True))
lista = list(apariciones)
print (lista)
