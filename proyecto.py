#Entrega2ci2691AbrJul118_15-10088_15-11138.py
# DESCRIPCION: Proyecto "Compositor Musical" de laboratorio de Algoritmos y Estrucutras 1
#	Luis Alfonso Pino y Félix Arnos
# Ultima modificacion: 07/07/2018
# VARIABLES:
#	e: int // ENTRADA: Opcion del menu principal a utilizar

######################################################### Librerias ################################################

import sys #Librería que nos permite relizatr el final del programa
import os #Librería utilizada en la interfaz de terminal para limpiar la pantalla 
from music21 import * #Librería base del proyecto
from pygame import * #Librería base del proyecto

######################################################## Variables #################################################

global partes #Aqui definimos el arreglo como global para usarlo en las funciones
partes=['','','',''] #Arreglo donde se guardan los archvos de las partes
e=0 # Variable de entrada del menu inicial

################################################## Funciones y Procedimientos #######################################

def MenuComposición (x:int) -> 'void':
	#Precondición: 0<y<7
	#Postcondición: True 
	global partes #Declaramos el arreglo global "partes" donde se guardan las partes que se registran en el programa

	os.system('clear') #Utilizamos esta función para limpiar la pantalla de la terminal y solo se vea el menú en ejecución
	print("---------------------------------------------")
	print("                MENU PRINCIPAL               ")
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

	#Procedemos a continuar la función dependiendo de la opción seleccionada por el usuario, es decir que en cada opción
	#seleccionada, filtrando con un condicional, se decide a cual función llamar según la decisión del usuario

	if (0<y<5):
		RegistroPartes(y)
	elif(y==5):	
		EscucharCancion(x)
		MenuComposición(x)
	else:
		#Se utiliza la librería Sys para poder finalizar el programa
		sys.exit()
def RegistroPartes(x:int) -> 'void':
	#Precondición: 0<y<7
	#Postcondición: True
	
	global partes #Declaramos el arreglo global "partes" donde se guardan las partes que se registran en el programa

	os.system('clear') #Utilizamos esta función para limpiar la pantalla de la terminal y solo se vea el menú en ejecución
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
	#Procedemos a continuar la función dependiendo de la opción seleccionada por el usuario, es decir que en cada opción
	#seleccionada, filtrando con un condicional, se decide a cual función llamar según la decisión del usuario. Cada una de
	#estas corresponde a un subprograma funcional, es decir que ejecuta una opción, no un menú de opciones para ser elegidas

	if (y==1):
		Registrar(x)
	elif(y==2):
		Arpegio(x) 
	elif(y==3):
		transporte(x) 
	elif(y==4):
		Reproduciendo(x)
	elif(y==5):
		Borrar(x)
	else:
		MenuComposición(x) # En caso de que el usurio lo solicite, se regresa al menú previo
def transporte(x:int) -> 'void':
	
	global partes #Declaramos el arreglo global "partes" donde se guardan las partes que se registran en el programa
	d=''

	#Se Solicita la entrada del intervalo de transporte de manera Robusta, así en caso de errores, la persona puede
	#continuar ingesando un valor de intervalo hasta que sea admisible. E igualmente en caso de que el intervalo 
	#solcitiado no coincida con un valor aceptado por la librería, igualmente dará un mensaje de error y permitirá
	#reintroducir los datos 

	os.system('clear') #Utilizamos esta función para limpiar la pantalla de la terminal y solo se vea el menú en ejecución
	print("Estos son los intervalos de transporte disponibles-:")
	print("P1     M2     m2     M3     M3     P4")
	print("P5     M6     m6     M7     m7     P8")

	#En la parte superior le damos al usuario las opciones de intervalo de trasnporte que nuestro programa ofrece para evitar
	#confusiones y errores por introducir un intervalo erroreo

	#Se Solicita la entrada del intervalo de manera Robusta, así en caso de errores, la persona puede
	#continuar ingesando numeros hasta que este el valor correcto
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
	
	#Utilizando un condicional verificamos que existe una parte registrada para realizar el transporte. En caso de no existir
	#Muestra un mensaje de error y regresa al menú anterior. En caso de existir, se realiza el proceso de transporte

	if (partes[x-1]==''):
		print("No existe una parte registrada")
		time.delay(5000)
	else:
		d=c+str(i)#Convertimos el valor entero que introdujo el usuario para poder realizar el transporte	
		sp = partes[x-1].transpose(d) #Función de music21 que realiza el transporte
		partes[x-1]=sp
		print("El transporte se realizó exitosamente")
		time.delay(5000)
	
	RegistroPartes(x) # Regresamos al menú anterior para que el usuario decida la siguiente acción
def Arpegio(x:int) -> 'void':
	global partes #Declaramos el arreglo global "partes" donde se guardan las partes que se registran en el programa
	os.system('clear') #Utilizamos esta función para limpiar la pantalla de la terminal y solo se vea el menú en ejecución
	
	#Se Solicita la entrada de la nota inicial de manera Robusta, así en caso de errores, la persona puede
	#continuar ingesando numeros hasta que este el valor correcto
	while True:
		try:
			a=input("Introduzca el tono inicial del arpegio: ")
			b=int(input("Introduzca la escala de dicho tono: "))
			assert((a=='A'or a=='B' or a=='C'or a=='D' or a=='E' or a=='F' or a=='G') and (0<b<8))
			print("Nota Registrada")
			print("")
			break
		except:
			print("Este tono no es valido, por favor intentelo nuevamente")


	#Se Solicita la entrada del Intervalo de Trasnsporte de manera Robusta, así en caso de errores, la persona puede
	#continuar ingesando numeros hasta que este el valor correcto

	print("Estos son los intervalos de transporte disponibles-:")
	print("P1     M2     m2     M3     M3     P4")
	print("P5     M6     m6     M7     m7     P8")
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

	arpegio = stream.Part() #Generamos un archivo de tipo part para agregar las notas del arpegio
	nota = note.Note(No) #Damos el atributo de Nota a la varible "nota" para realizar el arpegio

	#Utilizando un ciclo for se agregan las notas que van siendo transportadas al arpegio para que luego sea guardado en una
	#parte

	for i in range(0, 8):
		arpegio.append(nota)
		nota = nota.transpose(h)

	partes[x-1] = arpegio #Asignamos a la parte correspondiente el arpegio ya creado
	os.system('clear') #Utilizamos esta función para limpiar la pantalla de la terminal y solo se vea el mensaje en pantalla
	print("El arpegio ha sido creado exitosamente")
	time.delay(5000)
	RegistroPartes(x)
def EscucharCancion(x:int) -> 'void':
	cancion=stream.Score() #Creaamos un valor stream.Score que nos reproducirá todas las partes en paralelo

	#Con un ciclo for unimos la parte al objeto canción. Este ciclo realiza el filtro con un If: Si la parte esta registrada
	#Entonces esta es agregada al Score, de lo contrario esta parte del arreglo es ignorada y se evalua la siguiente

	for i in range(0,4):
		if (partes[i]!=''):
			cancion.insert(0,partes[i])
		else:
			pass

	sp = midi.realtime.StreamPlayer(cancion) #Creamos un archivo Midi temporal para reproducir
	os.system('clear') #Utilizamos esta función para limpiar la pantalla de la terminal y solo se vea el mensaje en pantalla
	print("Reproduciendo composición completa")
	sp.play() #reproducimos la composición completa
def Registrar(x:int) -> 'void':
	os.system('clear') #Utilizamos esta función para limpiar la pantalla de la terminal y solo se vea el menú en ejecución
	
	#Se Solicita la entrada de la entrada del archivo de manera Robusta, así en caso de errores, la persona puede
	#continuar ingesando numeros hasta que este el valor correcto

	while True:
			try:
				z=str(input("Introduzca el nombre exacto del archivo a reporducir: "))
				partes[x-1] = converter.parse(z) #Convertimos el archivo de texto "Tinynotation" en un archivo part de music21
				break
			except:
				print("El archivo no existe, intente de nuevo")
		
	os.system('clear') #Utilizamos esta función para limpiar la pantalla de la terminal y solo se vea el mensaje en pantalla
	print("---------------------------------------------------------")
	print("El archivo fue cargado de manera exitosa en la parte ",x)
	print("---------------------------------------------------------")
	time.delay(5000)

	RegistroPartes(x)
def Reproduciendo(x:int) -> 'void':
	#Primero verificamos si la parte que el usurio desea ya tiene un registro
	os.system('clear') #Utilizamos esta función para limpiar la pantalla de la terminal y solo se vea el menú en ejecución
	if (partes[x-1]==''):
		#En este caso, en el arreglo donde se guardan las partes no posee ninguna "part" registrada, por ende se informa			
		print("Esta parte aun no tiene registro")
		time.delay(5000)
		RegistroPartes(x)
	else:
			#En este caso ya existe una parte registrada, se procede a realizar la reproedyucción de la melodía 
		try:
			sp = midi.realtime.StreamPlayer(partes[x-1])
			print("Reproduciendo...")
		except:
			print("Esta parte no se puede reproducir")
			time.delay(5000)
			RegistroPartes(x)
			
		sp.play()

	

	RegistroPartes(x) # Regresamos al menú anterior para que el usuario decida la siguiente acción
def Borrar(x:int) -> 'void':
	partes[x-1] = '' #Sustituimos el contenido de esta parte del arreglo por un espacio vacio de tipo string, así el
					 #contenido que había sido registrado ene sta parte es eliminado
	os.system('clear') #Utilizamos esta función para limpiar la pantalla de la terminal y solo se vea el menú en ejecución
	print("Esta parte ha sido borrada exitosamente")
	time.delay(5000)
	RegistroPartes(x) # Regresamos al menú anterior para que el usuario decida la siguiente acción

################################################### Programa Principal ############################################## 

os.system('clear')
print("---------------------------------------------")
print("      Bienvenido al compositor musical")
print("---------------------------------------------")
print("Seleccione la opción que desea realizar:")
print("	1-.Iniciar")
print("	2-.Salir")

#Precondición
#Se Solicita la entrada del menú de manera Robusta, así en caso de errores, la persona puede
#continuar ingesando numeros hasta que este el valor correcto
while True:
	try:
		e=int(input("Inserte la opción que considere: "))
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