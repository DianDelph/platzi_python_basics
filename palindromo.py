#averigua si una palabra es palíndromo o no


def palindromo(palabra):
	#quito espacios reemplazándolos por chars vacíos
	palabra = palabra.replace(' ', '')
	#pasamos la palabra a mínusculas, para la compu L y l son direntes chars
	palabra = palabra.lower()
	#invierto la palabra y la guardo en una variable
	palabra_invertida = palabra[::-1]
	#pregunto si ambas palabras son iguales
	if palabra == palabra_invertida:
		return True
	else:
		return False


#buena práctica para correr los programas
def run():
	#pido al usuario una palabra
	palabra = input('Escribe una palabra ')
	#invoco la función que comprueba si es o no 
	es_palidromo = palindromo(palabra)

	if es_palidromo == True: # si es palíndromo
		print(palabra + ' es un palíndromo')
	else: #si no es
		print(palabra + ' no es un palíndromo')


#punto de entrada de python
if __name__ == "__main__":
	run()