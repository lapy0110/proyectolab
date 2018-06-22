############################################# Librerias ############################################3

import sys
from music21 import *
from pygame import *

######################################## Declaración Variables ####################################

e=0

##################################################### Funciones ##########################################

def MenuComposición (x) -> 'void':
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
		print("Esta función aun no ha sido codeada")
		MenuComposición(x)
	else:
		#Se utiliza la librería Sys para poder finalizar el programa
		sys.exit()

#--------------------------------------------------------------------------------------
def RegistroPartes(x) -> 'void':
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
		print("Esta opción carga un archivo")
	elif(y==2):
		print("Esta opción genera un arpegio")
	elif(y==3):
		print("Esta opción realiza un transporte")
	elif(y==4):
		print("Esta opción hace que se escuche esta parte")
	elif(y==5):
		print("Esta parte borra toda la composición")
	else:
		MenuComposición(x)

#--------------------------------------------------------------------------------------

##########################################################Main#####################################################
print("Bienvenido al compositor musical de Pino y Felix")
print("Seleccione la opción que desea realizar:")
print("	1-.Cargar Composición")
print("	2-.Salir")

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


if (e==1):
	#Se ingresa al submenú donde aparecen las opciones de la composición
	MenuComposición(e)
elif(e==2):
	#Se utiliza la librería Sys para finalizar el programa
	sys.exit()






