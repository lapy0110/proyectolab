#Entrega1ci2691AbrJul118_15-10088_15-11138.py
# DESCRIPCION: Primera fase del proyecto "Compositor Musical" de laboratorio de algoritmos 1
#	Luis Alfonso Pino y Félix Arnos
# Ultima modificacion: 23/07/2018
# VARIABLES:
#	e: int // ENTRADA: Opcion del menu principal a utilizar

#Librerias 

import sys
from music21 import *
from pygame import *

#Variables

e=0 # Variable de entrada del menu inicial

#Funciones y Procedimientos

def MenuComposición (x) -> 'void':
	#Precondición: 0<y<7
	#Postcondición: True 
	print("")
	print("---------------------------------------------")
	print("1-. Registrar Parte 1")
	print("2-. Registrar Parte 2")
	print("3-. Registrar Parte 3")
	print("4-. Registrar Parte 4")
	print("5-. Escuchar Composición")
	print("6-. Salir")
	
	#Se Solicita la entrada del menú de manera Robusta, así en caso de errores, la persona puede
	#continuar ingesando numeros hasta que este el valor correcto

	while True:
		try:
			y=int(input("Introduzca la opción que considere: "))
			assert(0<y<7)
			break
		except:
			print("Esta opción no esta dentro del menú")
			print("Vuelve a intentar")

	#Procedemos a continuar la función dependiendo de la opción seleccionada por el usuario

	if (0<y<5):
		RegistroPartes(y)
	elif(y==5):
		print("Esta función permite escuchar la composición completa")
		MenuComposición(x)
	else:
		#Se utiliza la librería Sys para poder finalizar el programa
		sys.exit()

#--------------------------------------------------------------------------------------
def RegistroPartes(x) -> 'void':
	#Precondición: 0<y<7
	#Postcondición: True
	print("")
	print("---------------------------------------------")
	print("          ESTAS EN EL MENU DE LA PARTE ",x)
	print("---------------------------------------------")
	print("1-. Cargar de un archivo")
	print("2-. Generar arpegio")
	print("3-. Transportar")
	print("4-. Escuchar parte")
	print("5-. Borrar parte")
	print("6-. Volver ")
	
	#Se Solicita la entrada del menú de manera Robusta, así en caso de errores, la persona puede
	#continuar ingesando numeros hasta que este el valor correcto

	while True:
		try:
			y=int(input("Introduzca la opción que considere: "))
			assert(0<y<7)
			break
		except:
			print("Esta opción no esta dentro del menú")
			print("Vuelve a intentar")
	#Procedemos a continuar la función dependiendo de la opción seleccionada por el usuario

	if (y==1):
		while True:
			try:
				z=str(input("Introduzca el nombre exacto del archivo a reporducir: "))
				s = converter.parse(z)
				break
			except:
				print("El archivo no existe, intente de nuevo")
		
		sp = midi.realtime.StreamPlayer(s)
		
		print("Reproduciendo",z,"...")
		sp.play()
		RegistroPartes(x)

	elif(y==2):
		print("Esta opción genera un arpegio")
		RegistroPartes(x)
	elif(y==3):
		print("Esta opción realiza un transporte")
		RegistroPartes(x)
	elif(y==4):
		print("Esta opción hace que se escuche esta parte")
		RegistroPartes(x)
	elif(y==5):
		print("Esta parte borra toda la composición")
		RegistroPartes(x)
	else:
		MenuComposición(x)

#--------------------------------------------------------------------------------------

#Programa Principal

print("Bienvenido al compositor musical")
print("Seleccione la opción que desea realizar:")
print("	1-.Cargar Composición")
print("	2-.Salir")

#Precondición
#Se Solicita la entrada del menú de manera Robusta, así en caso de errores, la persona puede
#continuar ingesando numeros hasta que este el valor correcto
while True:
	try:
		e=int(input("Inserte la opicón que considere: "))
		assert(0<e<3)
		break
	except:
		print("Esta opción no esta dentro del menú")
		print("Vuelve a intentar")

#Calculos
if (e==1):
	#Se ingresa al submenú donde aparecen las opciones de la composición
	MenuComposición(e)
elif(e==2):
	#Se utiliza la librería Sys para finalizar el programa
	sys.exit()

#Postcondición
assert(True)