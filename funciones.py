#introducción a funciones

#las funciones sirven para no repetir código
#los parámetros -lo que está entre ()- son variables que se mandan a las funciones para que éstas se ejecuten de acuerdo al valor de esa variable
#imprimir_mensaje recibe tiene el parámetro numero
def imprimir_mensaje(numero):
	print('Hola')
	print('Cómo estas?')
	#f-string sirve para mezclar variables con strings
	print(f'Elegiste la opción {numero}') 
	print('Adios')


opcion = int(input('Elige una opción (1,2,3)'))

#pregunto si la opcion elegida es 1, 2 o 3
if opcion == 1 or opcion == 2 or opcion == 3:
	#invoco la función y le paso "opcion" para que personalice el mensaje
	imprimir_mensaje(opcion) 
else: # si la opción no es 1,2 o 3
	print('Opcion incorrecta, adiós')