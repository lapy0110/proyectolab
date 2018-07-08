#Entrega2ci2691AbrJul118_15-10088_15-11138.py
# DESCRIPCION: Proyecto "Compositor Musical" de laboratorio de Algoritmos y Estrucutras 1
#	Luis Alfonso Pino y Félix Arnos
# Ultima modificacion: 07/07/2018
# VARIABLES:
#	e: int // ENTRADA: Opcion del menu principal a utilizar

######################################################### Librerias ################################################

import sys
from tkinter import *
from music21 import *
from pygame import *

####################################################### Interfaz Grafica ###########################################

#Ventana inicial

#Ventana
raiz= Tk() #Definimos la ventana raiz de nuestro programa
raiz.geometry('300x200') #Definimos el tamaño que tendra nuestra ventana
raiz.title('Compositor Musical') #Definimos el titulo de la ventana principal

#Botones
ttk.Button(raiz, text='Salir',command=quit).pack(side=bottom)
raiz.mainloop()

######################################################## Variables #################################################

global partes #Aqui definimos el arreglo como global para usarlo en las funciones
partes=['','','',''] #Arreglo donde se guardan los archvos de las partes
e=0 # Variable de entrada del menu inicial

################################################## Funciones y Procedimientos #######################################

def MenuComposición (x) -> 'void':
	#Precondición: 0<y<7
	#Postcondición: True 
	global partes #Declaramos el arreglo global "partes" donde se guardan las partes que se registran en el programa

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
	
	global partes #Declaramos el arreglo global "partes" donde se guardan las partes que se registran en el programa

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
		Arpegio(x) #Hacemos el llamado a la función Arpegio donde se realiza el proceso de creación de un arpegio para guardarlo
		#en la parte que solicite el usuario

	elif(y==3):
		transporte(x) #Hacemos el llamado a la función Transporte donde se realiza el transprote de la melodía solciitada por el
		#usuario

	elif(y==4):

		#Primero verificamos si la parte que el usurio desea ya tiene un registro
		if (partes[x-1]==''):
			#En este caso, en el arreglo donde se guardan las partes no posee ninguna "part" registrada, por ende se informa
			print("Esta parte aun no tiene registro")
			RegistroPartes(x)
		else:
			#En este caso ya existe una parte registrada, se procede a realizar la reproedyucción de la melodía 
			try:
				sp = midi.realtime.StreamPlayer(partes[x-1])
				print("Reproduciendo...")
			except:
				print("Esta parte no se puede reproducir")
				RegistroPartes(x)
			
			sp.play()

		RegistroPartes(x) # Regresamos al menú anterior para que el usuario decida la siguiente acción

	elif(y==5):
		partes[x-1] = '' #Sustituimos el contenido de esta parte del arreglo por un espacio vacio de tipo string, así el
		#contenido que había sido registrado ene sta parte es eliminado
		print("Esta parte ha sido borrada exitosamente")
		RegistroPartes(x) # Regresamos al menú anterior para que el usuario decida la siguiente acción

	else:
		MenuComposición(x) # En caso de que el usurio lo solciite, se regresa al menú previo

#--------------------------------------------------------------------------------------
def transporte(x) -> 'void':
	
	global partes #Declaramos el arreglo global "partes" donde se guardan las partes que se registran en el programa
	d=''

	#Se Solicita la entrada del intervalo de transporte de manera Robusta, así en caso de errores, la persona puede
	#continuar ingesando un valor de intervalo hasta que sea admisible. E igualmente en caso de que el intervalo 
	#solcitiado no coincida con un valor aceptado por la librería, igualmente dará un mensaje de error y permitirá
	#reintroducir los datos 

	while  True:
		try:
			i=int(input("De que alto desea que sea el intervalo de transporte: "))
			c=input("Desea que este transporte sea Mayor (M), Menor (m) o exacto(p)?: ")
			assert(1<=i<=8 and c=='M' or c=='m' or c=='p' or c=='P') #Verificación de que los datos ingresados son correctos
			assert((c=='p' and (i==1 or i==4 or i==5 or i==8)) or ((c=='m' or c== 'M') and (i==2 or i==3 or i==6 or i==7 )))
			#En esta seguna aserción verificamos que la entrada de datos coincida con la tabla de intervalos de la libreria
			#Music21
			break
		except:
			print("Esta opción no es admitida, por favor ingrese una opción adecuada")
			
	if (partes[x-1]==''):
		print("No existe una parte registrada")
	else:
		d=c+str(i)#Convertimos el valor entero que introdujo el usuario para poder realizar el transporte	
		sp = partes[x-1].transpose(d)
		partes[x-1]=sp
		#Aqui queda pendiete filtrar los casos bases con un if o con Asserts
		print("El transporte se realizó exitosamente")
	
	RegistroPartes(x) # Regresamos al menú anterior para que el usuario decida la siguiente acción
#------------------------------------------------------------------------------------
def Arpegio(x:int) -> 'void':
	global partes #Declaramos el arreglo global "partes" donde se guardan las partes que se registran en el programa

	while True:
		try:
			a=input("Introduzca el tono inicial del arpegio: ")
			b=int(input("Introduzca la escala de dicho tono: "))
			assert((a=='A'or a=='B' or a=='C'or a=='D' or a=='E' or a=='F' or a=='G') and (0<b<8))
			break
		except:
			print("Este tono no es valido, por favor intentelo nuevamente")


	while  True:
		try:
			i=int(input("De que alto desea que sea el intervalo de transporte: "))
			c=input("Desea que este transporte sea Mayor (M), Menor (m) o exacto(p)?: ")
			assert(1<=i<=8 and c=='M' or c=='m' or c=='p' or c=='P') #Verificación de que los datos ingresados son correctos
			assert((c=='p' and (i==1 or i==4 or i==5 or i==8)) or ((c=='m' or c== 'M') and (i==2 or i==3 or i==6 or i==7 )))
			#En esta seguna aserción verificamos que la entrada de datos coincida con la tabla de intervalos de la libreria
			#Music21
			break
		except:
			print("Esta opción no es admitida, por favor ingrese una opción adecuada")

	
	No = a + str(b) #Utilizando la entrada del usuario generamos una nota incial para el arpegio
	h = c + str(i) #Utilizando la entrada del usuario generamos el intervalo de transporte del arpegio

	arpegio= stream.Part()
	nota=note.Note(No) #Damos el atributo de Nota a la varible "nota" para realizar el arpegio

	for i in range(0, 8):
		arpegio.append(nota)
		nota = nota.transpose(c)

	partes[x-1] = arpegio
		
	
################################################### Programa Principal ############################################## 

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