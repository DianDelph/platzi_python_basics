#regresa si un numero es primo o no

def is_prime(number):
	#asumimos que el número es primo, por lo tanto no vamos a contar el 1 
	#ni al númermo mismo y el ciclo irá del 2 a uno antes del número
	for i in range(2, number):
		#pregunto si el residuo del número entre el iterador es 0
		if number % i == 0:
			#si lo es, cotinua el ciclo, termino el ciclo. 
			# con una división sin residuo tenemos, el número no es primo.
			return False
	#si nunca se rompió el ciclo, el número es primo.
	return True
			



def run():
	#mensaje de bienvenida
	message = "Escribe un número mayor a 1 para saber si es primo o no "
	#mensaje para seguir o no
	continue_message = """
	Continuar -> a
	Salir -> cualquier tecla
	"""
	exit_message = 'Saliendo...'
	
	#creo el ciclo para preguntar hasta que el usuario quiera salir
	option = input(continue_message)
	while option == 'a':
		#pido el número
		number = input(message)
		#compruebo que si fue un número
		if number.isdigit():
			#convierto la cadena número a entero
			number = int(number)
			#verificamos que el número si sea mayor a 1
			if number > 1:
				#invoco la función para saber si es primo o no
				if is_prime(number):
					print(f'{number} es un número primo')
				else:
					print(f'{number} no es un número primo')
			else: # si es 1 o menor, rompo el ciclo
				print('Error... ' + exit_message)
				break;
		else: #rompo el ciclo si el usuario no ingresó un número y salgo del programa
			print('Error... ' + exit_message)
			break;
		option = input(continue_message)
	
	#termina el ciclo, salgo del programa
	print(exit_message)

if __name__ == "__main__":
	run()