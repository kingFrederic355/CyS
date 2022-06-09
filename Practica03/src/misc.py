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
    max = mcd(a,m)
    if(max != 1):
        print('No tiene solucion')
        print(max,a,m)
        return -1
    
    if (m == 1):
        return 0
    
    while (a > 1):
        #print(m)
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

def binaryList(num):
    result = []
    while(num > 0):
        result.append(num%2)
        num = num//2
    return result