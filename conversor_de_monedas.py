#convierte pesos mexicanos a dólares

#pregunto al usuario la cantidad a convertir
pesos_mexicanos = input('¿Cuántos pesos mexicanos tienes?: ')

#convierto a float para mejor manejo de datos
pesos_mexicanos = float(pesos_mexicanos)

#escribo el valor del dolar en pesos mexicanos
tipo_de_cambio = 21.5

#hago la conversión
dolares = pesos_mexicanos / tipo_de_cambio

#convierto el float de dolares a un string
dolares = str(dolares)

#imprimo el valor de la conversion. Se pueden sumar (concatenar) strings con '+'
print('Tienes $' + dolares +' dólares')
