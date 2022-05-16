# REvisamos si es un residuo cuadratico
def quad_residue(a,n):
    l=1
    q=(n-1)//2
    x = q**l
    if x==0:
        return 1
        
    a =a%n
    z=1
    while x!= 0:
        if x%2==0:
            a=(a **2) % n
            x//= 2
        else:
            x-=1
            z=(z*a) % n

    return z


def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b, a%b)

# Devuelve k tal que b^k = 1 (mod p)
def order(p,q):
	if gcd(p,q) !=1:
		print(p,' and ',q,'are not co-prime')
		return -1
	k=3
	while True:
		if pow(q,k,p)==1:
			return k
		k+=1


def convertx2e(x):
	e=0
	while x%2==0:
		x/=2
		e+=1
	return int(x),e

#   Función principal para encontrar la raíz cuadrada modular
def STonelli(n, p): 
    assert quad_residue(n, p) == 1, "no es un cuadrado (mod p)"
    q = p - 1
    s = 0
    
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        r = pow(n, (p + 1) // 4, p)
        return r,p-r
    for z in range(2, p):
        #print(quad_residue(z, p))
        if p - 1 == quad_residue(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i

    return (r,p-r)

def main():
	n=2
	p=113
	print(STonelli(n,p))


if __name__ == '__main__':
	main()