'''Escribir una función ``es_vocal(caracter)`` 
que tome un carácter y devuelva un valor logico(True si es una vocal, de lo contrario devuelve False)
'''

def es_vocal(caracter):

    vocales = ['a','A','e','E','i','I','o','O','u','U']
    valor = True if caracter in vocales else False

    return valor

print(es_vocal('a'))
print(es_vocal(1))
print(es_vocal('H'))
print(es_vocal({}))

