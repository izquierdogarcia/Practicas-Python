# -*- coding: utf-8 -*- 

import string

#Convertir cada elemento de una lista a entero.
def list_to_int(l):
    return int("".join(str(x) for x in l))

respuesta = 0
numeros = []
while (respuesta != '5'):
	print 'CALCULADORA SENCILLA'
	print 'Elige la operación a realizar:'
	print '1. Sumar'
	print '2. Restar'
	print '3. Multiplicar'
	print '4. Dividir'
	print '5. SALIR'	

	try:
	    respuesta = int(raw_input('Opción: '))
	except:
		print "No es un número"
	else:
		if respuesta == 5: 
			break	

	    
		n = 0
		if respuesta > 0 and respuesta < 5:
			numeros = raw_input('Introduce los dígitos separados por un espacio: ')
			numeros = numeros.split(' ')
	        try:
	            list_to_int(numeros)
	        except:
		        print "No son números."
	        else:
			    for resultado in numeros:
					if respuesta == 1:
					    n = n + int(resultado)
					elif respuesta == 2: 
						if n == 0:
						    n = int(resultado)
						else:
							n = n - int(resultado)
					elif respuesta == 3:
						if n == 0:
						    n = int(resultado)
						else:
							n = n * int(resultado)
					elif respuesta == 4:
					    if n == 0:
						    n = int(resultado)
					    else:
						    n = n / int(resultado)
					

			    print n
	



