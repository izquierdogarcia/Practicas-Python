# -*- coding: utf-8 -*- 

import string

def list_to_int(l):
    return int("".join(str(x) for x in l))

print 'CALCULADORA SENCILLA'
print 'Elige la operación a realizar:'
print '1. Sumar'
print '2. Restar'
print '3. Multiplicar'
print '4. Dividir'

respuesta = raw_input('Opción: ')


numeros = raw_input('Introduce los dígitos separados por un espacio: ')



numeros = numeros.split(' ')
list_to_int(numeros)




n = 0
for resultado in numeros:
	if respuesta == '1':
	    n = n + int(resultado)
	if respuesta == '2': 
		if n == 0:
		    n = int(resultado)
		else:
			n = n - int(resultado)
	if respuesta == '3':
		if n == 0:
		    n = int(resultado)
		else:
			n = n * int(resultado)
	if respuesta == '4':
	    if n == 0:
		    n = int(resultado)
	    else:
		    n = n / int(resultado)


print n



