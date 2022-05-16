import msc
from random import randint

# Realice la prueba de primalidad de Rabin-Miller para determinar si el número dado es primo.
def is_probable_prime(a):
    
    if a == 2:
        return True

    if a == 1 or a % 2 == 0:
        return False

    return rmprimality(a, 50)

# Prueba de Miller Rabin 
def rmprimality(a, iterations):
    
    r, s = 0, a - 1

    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(iterations):
        n = randint(2, a - 1)
        x = pow(n, s, a)
        if x == 1 or x == a - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, a)
            if x == a - 1:
                break
        else:
            return False
    return True
# Comprueba si el entero dado es una potencia perfecta. 
def check_perfect_power(n):
    prime = small_primes[-1]
    for p in small_primes:
        pth_root = msc.kth_iroot(n, p)
        if pth_root < prime:
            break
        if pth_root ** p == n:
            return (pth_root, p)
    return None

# Comprueba si 'i' es un factor de 'n' y agrega 'i' a 'factores' si es verdadero por división de prueba
def check_factor(n, i, factors):
    
    while n % i == 0:
        n //= i
        factors.append(i)
        if is_probable_prime(n):
            factors.append(n)
            n = 1
    return n

# Realice una división de prueba en el número dado usando todos los números primos hasta el límite superior.
def find_small_primes(n, upper_bound):
    
    print("División de prueba e inicialización de primos pequeños...")
    global small_primes
    is_prime = [True] * (upper_bound + 1)
    is_prime[0:2] = [False] * 2
    factors = []
    small_primes = []
    max_i = msc.isqrt(upper_bound)
    rem = n
    for i in range(2, max_i + 1):
        if is_prime[i]:
            small_primes.append(i)
            rem = check_factor(rem, i, factors)
            if rem == 1:
                return factors, 1

            for j in range(i ** 2, upper_bound + 1, i):
                is_prime[j] = False

    for i in range(max_i + 1, upper_bound + 1):
        if is_prime[i]:
            small_primes.append(i)
            rem = check_factor(rem, i, factors)
            if rem == 1:
                return factors, 1

    print("Primos creados!")
    return factors, rem

# Devuelve uno o más factores primos del número dado n. 
def find_prime_factors(n):
    
    print("Revisando si {} es una potencia perfecta ...".format(n))
    perfect_power = check_perfect_power(n)
    if perfect_power:
        print("{} is {}^{}".format(n, perfect_power[0], perfect_power[1]))
        factors = perfect_power[0]
    else:
        print("No es potencia")
        digits = len(str(n))
        if digits <= 30:
            print("Usando la variante de Brent de la factorización rho de Pollard " + \
                  "algoritmo para factorizar {} ({} digitos)".format(n, digits))
            factors = [brent_factorise(n)]
        else:
            print("Uso de la criba cuadrática autoinicializante para factorizar " + \
                  "{} ({} digitos)".format(n, digits))
            #factors = siqs_factorise(n)

    prime_factors = []
    for f in set(factors):
        for pf in find_all_prime_factors(f):
            prime_factors.append(pf)

    return prime_factors

# Devuelve todos los factores primos del número dado n
def find_all_prime_factors(n):
    
    rem = n
    factors = []

    while rem > 1:
        if is_probable_prime(rem):
            factors.append(rem)
            break

        for f in find_prime_factors(rem):
            print("Factor primo encontrado: {}".format(f))
            assert is_probable_prime(f)
            assert rem % f == 0
            while rem % f == 0:
                rem //= f
                factors.append(f)

    return factors

# Funcion de Brent
def _pollard_brent_func(c, n, x):
    
    y = (x ** 2) % n + c
    if y >= n:
        y -= n

    assert y >= 0 and y < n
    return y

# Factorizacion usando el algoritmo de brent
def brent_factorise(n, iterations=None):
    
    y, c, m = (randint(1, n - 1) for _ in range(3))
    r, q, g = 1, 1, 1
    i = 0
    while g == 1:
        x = y
        for _ in range(r):
            y = _pollard_brent_func(c, n, y)
        k = 0
        while k < r and g == 1:
            ys = y
            for _ in range(min(m, r - k)):
                y = _pollard_brent_func(c, n, y)
                q = (q * abs(x - y)) %  n
            g = msc.gcd(q, n)
            k += m
        r *= 2
        if iterations:
            i += 1
            if i == iterations:
                return None

    if g == n:
        while True:
            ys = _pollard_brent_func(c, n, ys)
            g = msc.gcd(abs(x - ys), n)
            if g > 1:
                break
    return g

# Función de iterador para la variante de Brent para encontrar todos los factores primos pequeños.
def pollard_brent_iterator(n, factors):
    
    rem = n
    while True:
        if is_probable_prime(n):
            factors.append(n)
            rem = 1
            break

        digits = len(str(n))
        if digits < 45:
            iterations = 20
        else:
            iterations = 25

            f = brent_factorise(rem, iterations)
            if f and f < rem:
                if is_probable_prime(f):
                    print("Brent (rho de Pollard): Factor primo encontrado: " + \
                        "{}".format(f))
                    factors.append(f)
                    rem //= f
                else:
                    print("Brent (rho de Pollard): factor compuesto " + \
                          "encontrado: {}".format(f))
                    rem_f = pollard_brent_iterator(f, factors)
                    rem = (rem // f) * rem_f
            else:
                break
    return rem

def factorise(n):
    if type(n) != int or n < 1:
        raise ValueError("El numero debe ser un entero positivo")

    print("Factorizando {} ({} digitos)...".format(n, len(str(n))))

    if n == 1:
        return []

    if is_probable_prime(n):
        return [n]

    factors, rem = find_small_primes(n, 1000000)

    if factors:
        print("Factores primos encontrados hasta ahora:")
        factors_temp = []
        for _ in factors:
            if _ not in factors_temp:
                factors_temp.append(_)
        print(*factors_temp, sep=', ')
    else:
        print("¡No se han encontrado factores pequeños!")

    if rem != 1:
        digits = len(str(rem))
        if digits > 30:
            print("Intentando la rho de Quick Pollard (variación de Brent) para " + \
                  "encontrar factores ligeramente más grandes...")
            rem = pollard_brent_iterator(rem, factors)
        if rem > 1:
            for f in find_all_prime_factors(rem):
                factors.append(f)

    factors.sort()
    assert msc.product(factors) == n
    for p in factors:
        assert is_probable_prime(p)
    return factors

def main():
    n = int(input("Introduzca el número a factorizar:"))
    result = factorise(n)
    new_result = []

    for _ in result:
        if _ not in new_result:
            new_result.append(_)

    print("\nFactores primos: {}".format(new_result))

if __name__ == '__main__':
    main()