# requisitos previos pip install pycryptodome
import random as rdm
from Crypto.Util import number
"""
Funcion iterativa para calcular la exponenciacion modular

Args:
    x: Valor del elemento al cual queremos sacar su potencia.
    y: Potencia a la que se elevara.
    p: Modulo dentro del cual se mantendra el exponente

Returns:
    Regresa el valor elevado y acotado por el exponente """

def power(x, y, p) :
	res = 1
	x = x % p
	if (x == 0) :
		return 0
	while (y > 0) :
		if ((y & 1) == 1) :
			res = (res * x) % p
		y = y >> 1
		x = (x * x) % p
	return res

"""
Funcion que devuelve un primo de 100 cifras

Returns:
    Un valor primo de 100 digitos """
def getPrime():
    n_length = 330
    primeNum = number.getPrime(n_length)
    return primeNum
"""
Funcion que devuelve un valor coprimo a un valor dado

Args:
    value: numero que usaremos para evaluar la coprimalidad

Returns:
    Regresa un entero coprimo de value """
def getCoPrime(value):
    e = rdm.randint(2,value)
    while(mcd(e,value)!=1):
        e = rdm.randint(0,value)
    return e
"""
Funcion phi para los numeros p y q

Args:
    p: valor primo
    q: valor primo

Returns:
    regresa la multiplicacion de (p-1)*(q-1)"""
def euler(p,q):
    return (p-1)*(q-1)

"""
Funcion para calcular el maximo comun divisor de dos numeros 

Args:
    a: entero positivo
    b: entero positivo

Returns:
    regresa el mcd entre a y b"""
def mcd(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

'''
Funcion para obtener el inverso modular de un numero usando el algortimo extendido de euclides
Funcion hecha por Nikita tiwari.
Args:
    a: valor al que queremos sacar su inverso
    m: modulo en el cual se trabajara
Returns
    un valor d, tal que, d*a ≅ 1 mod m
'''
def modInverse(a, m):
	m0 = m
	y = 0
	x = 1
	if (m == 1):
		return 0

	while (a > 1):

		# q es el cociente
		q = a // m
		t = m
        # m es el resto ahora
		m = a % m
		a = t
		t = y

		# Actualiza x y
		y = x - q * y
		x = t

	# Convertimos a x en positivo
	if (x < 0):
		x = x + m0

	return x

def string2ASCII(text):
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))
    return ascii_values