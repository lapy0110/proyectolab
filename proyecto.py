#Entrega1ci2691AbrJul118_15-10088_15-11138.py
# DESCRIPCION: Primera fase del proyecto "Compositor Musical" de laboratorio de algoritmos 1
#	Luis Alfonso Pino y Félix Arnos
# Ultima modificacion: 23/07/2018
# VARIABLES:
#	e: int // ENTRADA: Opcion del menu principal a utilizar

######################################## Librerias ################################################

import sys
from music21 import *
from pygame import *

######################################## Variables #################################################

global partes #Aqui definimos el arreglo como global para usarlo en las funciones
partes=['','','',''] #Arreglo donde se guardan los archvos de las partes
e=0 # Variable de entrada del menu inicial

################################## Funciones y Procedimientos #######################################

def MenuComposición (x) -> 'void':
	#Precondición: 0<y<7
	#Postcondición: True 
	global partes

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
	
	global partes

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
				#Aqui falta ver como anular la operación
				z=str(input("Introduzca el nombre exacto del archivo a reporducir: "))
				partes[x-1] = converter.parse(z)
				break
			except:
				print("El archivo no existe, intente de nuevo")
		
		print("El archivo fue cargado de manera exitosa en la parte ",x)
		RegistroPartes(x)

	elif(y==2):
		print("Esta opción genera un arpegio")
		RegistroPartes(x)
	elif(y==3):
		transporte(x)
	elif(y==4):
		try:
			sp = midi.realtime.StreamPlayer(partes[x-1])
			print("Reproduciendo...")
		except:
			print("Esta parte no se puede reproducir")
			RegistroPartes(x)
			
		sp.play()
		RegistroPartes(x)
	elif(y==5):
		partes[x-1] = ''
		print("Esta parte ha sido borrada exitosamente")
		RegistroPartes(x)
	else:
		MenuComposición(x)

#--------------------------------------------------------------------------------------
def transporte(x) -> 'void':
	
	global partes
	d=''

	while  True:
		try:
			i=int(input("De que alto desea que sea el intervalo de transporte: "))
			assert(1<=i<=8)
			break
		except:
			print("Este intervalo no puede ser procesado")
			print("Debe estar entre 1 y 8. Por favor vuela a intentar")
	
	while True:
		try:
			c=input("Desea que este transporte sea Mayor (M), Menor (m) o exacto(p)?: ")
			assert(c=='M' or c=='m' or c=='p' or c=='P')
			break
		except:
			print("Esta opción no es admitida, por favor ingrese una opción adecuada")

	d=c+str(i)#Convertimos el valor entero que introdujo el usuario para poder realizar el transporte
	print(partes[x-1])	
	sp = partes[x-1].transpose(d)
	print(sp)
	partes[x-1]=sp
	#Aqui queda pendiete filtrar los casos bases con un if o con Asserts
	print("El transporte se realizó exitosamente")
	RegistroPartes(x)


##################################### Programa Principal ############################################## 

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