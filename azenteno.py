# -*- coding: utf-8 -*-
import json
import sys
import bisect

with open('redd-test-data.json') as json_data:
	d = json.load(json_data)

try:
	sku = sys.argv[1]
	limite = int(sys.argv[2])
	base = d[sku]
except Exception as e:
	print "Ingresa Valores Correctos" 
	sys.exit(0)

'''
array y similares son matrices de coincidencias
en array se guardan los poderados de coincidencias y en similares, los objetos.

Ej en similares[4]  se guardarán todos los objetos que coinciden en 5 elementos
en similares[6] se guardarán todos los objetos que coinciden en 6 elementos.
Éstos son ordenados de acuerdo al nombre del atributo de manera ascendente
'''

array = []
similares =[]

keys = sorted(base.keys())
n = len(keys)

for i in range(n):
	array.append([])
	similares.append([])

for u in d:
	if u!=sku:
		contador = 0
		i = 0
		match = 0
		for k in keys:
			'''
			Si los atributos son iguales,
			pondera de acuerdo al orden alfabético
			'''
			if k in d[u]:
				if d[u][k] == base[k]:
					contador+=i
					match +=1
			i+=1
		'''
			Si el elemento no tiene ningún atributo en común, se excluye de la lista
			(menos pega)
			Si no, los agrego al arreglo de manera ordenada de acuerdo a su ponderación
		'''
		if match>0:
			indice = bisect.bisect(array[match-1],contador)
			array[match-1].insert(indice,contador);
			similares[match-1].insert(indice,d[u])
'''
	Ahora simplemente... los muestro...
'''

cont = 0
print json.dumps(base),
print "es mas parecido a "
for i in range(n):
	for x in similares[n-i-1]:
		print json.dumps(x),
		cont+=1
		if cont==limite:
			break
		else:
			print "(con "+str(n-i)+" coincidencias) que a"
	if cont==limite:
		break# -*- coding: utf-8 -*-
import json
import sys
import bisect

with open('redd-test-data.json') as json_data:
	d = json.load(json_data)

try:
	sku = sys.argv[1]
	limite = int(sys.argv[2])
	base = d[sku]
except Exception as e:
	print "Ingresa Valores Correctos" 
	sys.exit(0)

'''
array y similares son matrices de coincidencias
en array se guardan los poderados de coincidencias y en similares, los objetos.

Ej en similares[4]  se guardarán todos los objetos que coinciden en 5 elementos
en similares[6] se guardarán todos los objetos que coinciden en 6 elementos.
Éstos son ordenados de acuerdo al nombre del atributo de manera ascendente
'''

array = []
similares =[]

keys = sorted(base.keys())
n = len(keys)

for i in range(n):
	array.append([])
	similares.append([])

for u in d:
	if u!=sku:
		contador = 0
		i = 0
		match = 0
		for k in keys:
			'''
			Si los atributos son iguales,
			pondera de acuerdo al orden alfabético
			'''
			if k in d[u]:
				if d[u][k] == base[k]:
					contador+=i
					match +=1
			i+=1
		'''
			Si el elemento no tiene ningún atributo en común, se excluye de la lista
			(menos pega)
			Si no, los agrego al arreglo de manera ordenada de acuerdo a su ponderación
		'''
		if match>0:
			indice = bisect.bisect(array[match-1],contador)
			array[match-1].insert(indice,contador);
			similares[match-1].insert(indice,d[u])
'''
	Ahora simplemente... los muestro...
'''

cont = 0
print json.dumps(base),
print "es mas parecido a "
for i in range(n):
	for x in similares[n-i-1]:
		print json.dumps(x),
		cont+=1
		if cont==limite:
			break
		else:
			print "(con "+str(n-i)+" coincidencias) que a"
	if cont==limite:
		break
