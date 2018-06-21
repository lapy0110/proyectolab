#############################################Librerias

import sys
from music21 import *
from pygame import *

########################################Veclaración Variables####################################3

e=0

######################################################Funciones##########################################

def MenuSelect (x) -> 'void':
	if (x==1):
		MenuComposición(x)
	elif(x==2):
		sys.exit()

def MenuComposición (x) -> 'void':
	print("---------------------------------------------")
	print("1-. Registrar Parte 1")
	print("2-. Registrar Parte 2")
	print("3-. Registrar Parte 3")
	print("4-. Registrar Parte 4")
	print("5-. Escuchar Composición")
	print("6-. Salir")
	y=int(input("Introduzca la opción que considere: "))

	if (y==6):
		sys.exit()


##########################################################Main#####################################################
print("Bienvenido al compositor musical")
print("Seleccione la opción que desea realizar:")
print("	1-.Cargar Composición")
print("	2-.Salir")

e=int(input("Inserte la opicón que considere: "))
MenuSelect(e)






