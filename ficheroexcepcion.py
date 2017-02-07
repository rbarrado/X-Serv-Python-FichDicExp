#!/usr/bin/python

fich = open("/etc/passwd", "r");

lineas = fich.readlines()
diccionario = {}

for linea in lineas:
	elemento = linea.split(':')
	User = elemento[0]
	Shell = elemento[-1]
	diccionario[User] = Shell 


print"La shell de root es:", diccionario["root"]

try: 
	print(diccionario["imaginario"])
except:
	print('El nombre de usuario "imaginario" no existe.')
