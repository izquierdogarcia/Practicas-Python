# -*- coding: utf-8 -*- 

import string

#Convertir cada elemento de una lista a entero.
def list_to_int(l):
    return int("".join(str(x) for x in l))

respuesta = 0
while (respuesta != '5'):
	print 'CALCULADORA SENCILLA'
	print 'Elige la operación a realizar:'
	print '1. Sumar'
	print '2. Restar'
	print '3. Multiplicar'
	print '4. Dividir'
	print '5. SALIR'

	respuesta = raw_input('Opción: ')
	if respuesta == '5': 
		break


	
		numeros = raw_input('Introduce los dígitos separados por un espacio: ')
		numeros = numeros.split(' ')
		list_to_int(numeros)

	n = 0
	if respuesta > 0 and respuesta < 5:
		for resultado in numeros:
			if respuesta == '1':
			    n = n + int(resultado)
			elif respuesta == '2': 
				if n == 0:
				    n = int(resultado)
				else:
					n = n - int(resultado)
			elif respuesta == '3':
				if n == 0:
				    n = int(resultado)
				else:
					n = n * int(resultado)
			elif respuesta == '4':
			    if n == 0:
				    n = int(resultado)
			    else:
				    n = n / int(resultado)
			

		print n
	else:
		print "Elija la opción correcta."



