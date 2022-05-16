# Funciones extras para la resolucion de criba cuadratica

# Regresa el producto usando una lista dada
def product(list):
    
    prod = 1
    for elem in list:
        prod *= elem
    return prod

# Maximo comun divisor
def gcd(a, b):
    
    while b:
        a, b = b, a % b
    return a

# Devuelve la raíz k-ésima entera de un número por el método de Newton
def kth_iroot(n, k):
    u = n
    s = n + 1
    while u < s:
        s = u
        t = (k - 1) * s + n // pow(s, k - 1)
        u = t // k
    return s

# Funcion para la raiz cuadrada de un numero en entero
def isqrt(n):
   
    if n < 0:
        raise ValueError("Square root of negative number!")
    x = int(n)
    if n == 0:
        return 0
    a, b = divmod(x.bit_length(), 2)
    n = 2 ** (a + b)
    while True:
        y = (n + x // n) // 2
        if y >= x:
            return x
        x = y