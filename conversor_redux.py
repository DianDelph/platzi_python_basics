#convierte pesos mexicanos, argentinos y colombianos a dólares

#funcion que realiza la conversión

def convertir(pais, valor_dolar):
	#pregunto al usuario la cantidad a convertir
	pesos = input('¿Cuántos pesos ' + pais + ' tienes?: ')
	#convierto a float para mejor manejo de datos
	pesos = float(pesos)
	#hago la conversión
	dolares = pesos / valor_dolar
	#redondeo los dólares a dos decimales
	dolares = round(dolares, 3)
	#convierto el float de dolares a un string
	dolares = str(dolares)
	#imprimo el valor de la conversion. Se pueden sumar (concatenar) strings con '+'
	print('Tienes $' + dolares +' dólares')


# """ """ permite crear strings multilineas
menu = """
Bienvenido al conversor de monedas multipais

1-Pesos Mexicanos
2-Pesos Colombianos
3-Pesos Argentinos

Elige una opción: 

"""
# de derecha a izquierda: llamo a la funcion input, le paso la variable menu para que la imprima y reciba el número que el usuario escogió, lo convierto a int y lo guardo en la variable 'opcion'
opcion = int(input(menu))

if opcion == 1: #pesos mexicanos
	#invoco la función
	convertir('mexicanos',21.5)
elif opcion == 2: #pesos colombianos
	#invoco la función
	convertir('colombianos',3715.01)
elif opcion == 3: #pesos argentinos
	#invoco la función
	convertir('argentinos',74.44)
else:  #el usuario escribió algo diferente
	print('Escribe una opción correcta: ')


