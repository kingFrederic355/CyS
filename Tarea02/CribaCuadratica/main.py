from math import fabs, ceil, sqrt, exp, log
import random
from millerR import is_probable_prime
from shanks import STonelli
from itertools import chain

def gcd(a,b): # Algoritmo de euclides
    if b == 0:
        return a
    elif a >= b:
        return gcd(b,a % b)
    else:
        return gcd(b,a)

def isqrt(n): # Metodo de Newton
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def mprint(M): # Forma de visualizar agradable
    for row in M:
        print(row)
        
def prime_gen(n): # Criba de Eratóstenes, para primos hasta n
    if n < 2:
        return []
    
    nums = []
    isPrime = []
    
    for i in range(0, n+1):# Numeros desde 0 hasta n
        nums.append(i)
        isPrime.append(True)
        
    isPrime[0]=False
    isPrime[1]=False
    
    for j in range(2,int(n/2)):# prueba todos los espacios de tamaño que tienen sentido
        if isPrime[j] == True:
            for i in range(2*j,n+1,j):# comienza desde j+j, salta por el tamaño del espacio j y tacha ese número
                isPrime[i] = False
                
    primes = []
    for i in range(0, n+1):# Agrega los faltantes
        if isPrime[i] == True:
            primes.append(nums[i])
            
    return primes

# comprueba si a es un residuo cuádruple de n
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
        
def size_bound(N): # encuentra el tamaño e intervalo óptimos de la base factorial

    F = pow(exp(sqrt(log(N)*log(log(N)))),sqrt(2)/4)
    I = F**3
    return int(F),int(I)


    
def find_base(N,B):
# genera una base de 

    factor_base = []
    primes = prime_gen(B)
    
    for p in primes: # tal que N es un residuo cuadrático mod p
        if quad_residue(N,p) == 1:
            factor_base.append(p)
    return factor_base

# intenta encontrar números para la criba
def find_smooth(factor_base,N,I):
    
    # genera una secuencia de Y(x) = x^2 - N, comenzando en x = root
    def sieve_prep(N,sieve_int):
        sieve_seq = [x**2 - N for x in range(root,root+sieve_int)]
        return sieve_seq

    sieve_seq = sieve_prep(N,I)
    sieve_list = sieve_seq.copy()
    if factor_base[0] == 2:
        i = 0
        while sieve_list[i] % 2 != 0:
            i += 1
        for j in range(i,len(sieve_list),2): # numeros pares
            while sieve_list[j] % 2 == 0: # potencias de 2
                sieve_list[j] //= 2
                
    for p in factor_base[1:]:
        residues = STonelli(N,p) # Encuentre x tal que x^2 = n (mod p).
        
        for r in residues:
            for i in range((r-root) % p, len(sieve_list), p): # Now every pth term will also be divisible
                while sieve_list[i] % p == 0: #account for prime powers
                    sieve_list[i] //= p
    xlist = [] #original x terms
    smooth_nums = []
    indices = [] # index of discovery
    
    for i in range(len(sieve_list)):
        if len(smooth_nums) >= len(factor_base)+T: #probability of no solutions is 2^-T
            break
        if sieve_list[i] == 1: # found B-smooth number
            smooth_nums.append(sieve_seq[i])
            xlist.append(i+root)
            indices.append(i)

    return(smooth_nums,xlist,indices)

def build_matrix(smooth_nums,factor_base):
# generates exponent vectors mod 2 from previously obtained smooth numbers, then builds matrix

    def factor(n,factor_base):#trial division from factor base
        factors = []
        if n < 0:
            factors.append(-1)
        for p in factor_base:
            if p == -1:
                pass
            else:
                while n % p == 0:
                    factors.append(p)
                    n //= p
        return factors

    M = []
    factor_base.insert(0,-1)
    for n in smooth_nums:
        exp_vector = [0]*(len(factor_base))
        n_factors = factor(n,factor_base)
        #print(n,n_factors)
        for i in range(len(factor_base)):
            if factor_base[i] in n_factors:
                exp_vector[i] = (exp_vector[i] + n_factors.count(factor_base[i])) % 2

        #print(n_factors, exp_vector)
        if 1 not in exp_vector: #search for squares
            return True, n
        else:
            pass
        
        M.append(exp_vector)  
    #print("Matrix built:")
    #mprint(M)
    return(False, transpose(M))

    
def transpose(matrix):
#transpose matrix so columns become rows, makes list comp easier to work with
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row)
    return(new_matrix)
    
# reduced form of gaussian elimination    
def gauss_elim(M):
    
    marks = [False]*len(M[0])
    
    for i in range(len(M)): 
        row = M[i]
        
        for num in row: 
            if num == 1:
                j = row.index(num) 
                marks[j] = True
                
                for k in chain(range(0,i),range(i+1,len(M))): 
                    if M[k][j] == 1:
                        for i in range(len(M[k])):
                            M[k][i] = (M[k][i] + row[i])%2
                break
    
    M = transpose(M)
        
    sol_rows = []
    for i in range(len(marks)): 
        if marks[i]== False:
            free_row = [M[i],i]
            sol_rows.append(free_row)
    
    if not sol_rows:
        return("No se ha encontrado solucion.")
    print("Encuentra {} posibles soluciones".format(len(sol_rows)))
    return sol_rows,marks,M

def solve_row(sol_rows,M,marks,K=0):
    solution_vec, indices = [],[]
    free_row = sol_rows[K][0] # Puede ser multiplo de k
    for i in range(len(free_row)):
        if free_row[i] == 1: 
            indices.append(i)
    for r in range(len(M)): 
        for i in indices:
            if M[r][i] == 1 and marks[r]:
                solution_vec.append(r)
                break
            
    solution_vec.append(sol_rows[K][1])       
    return(solution_vec)
    
def solve(solution_vec,smooth_nums,xlist,N):
    
    solution_nums = [smooth_nums[i] for i in solution_vec]
    x_nums = [xlist[i] for i in solution_vec]
    
    Asquare = 1
    for n in solution_nums:
        Asquare *= n
        
    b = 1
    for n in x_nums:
        b *= n

    a = isqrt(Asquare)
    
    factor = gcd(b-a,N)
    return factor


def QS(n,B,I):
#versión polinomial simple de criba cuadrática, dado el límite de suavidad B y el intervalo de tamiz I
    
    global N
    global root
    global T # Factor de tolerancia
    N,root,K,T = n,int(sqrt(n)),0,1

    if is_probable_prime(N):
        return "Primo"
    
    if isinstance(sqrt(N),int):
        return isqrt(N)
        
    factor_base = find_base(N,B)
    
    global F
    F = len(factor_base)
    
    smooth_nums,xlist,indices = find_smooth(factor_base, N,I)
    #finds B-smooth relations, using sieving and Tonelli-Shanks
    
    print("Encontrando {} numeros.".format(len(smooth_nums)))
   
    print(smooth_nums)
    
    if len(smooth_nums) < len(factor_base):
        return("Faltan numeros.")
        
    is_square, t_matrix = build_matrix(smooth_nums,factor_base)
    
    if is_square == True:
        x = smooth_nums.index(t_matrix)
        factor = gcd(xlist[x]+sqrt(t_matrix),N)
        print("Se encontro una raiz!")
        return factor, N/factor
    
    print("Eliminacion Gausiana...")
    sol_rows,marks,M = gauss_elim(t_matrix) 
    solution_vec = solve_row(sol_rows,M,marks,0)
    
    print("Resolviendo congruencia de cuadrados...")
    factor = solve(solution_vec,smooth_nums,xlist,N)

    for K in range(1,len(sol_rows)):
        if (factor == 1 or factor == N):
            print("No funciono...")
            solution_vec = solve_row(sol_rows,M,marks,K)
            factor = solve(solution_vec,smooth_nums,xlist,N)
        else:
            print("Factores encontrados!")
            return factor, int(N/factor)
            
            
    return("No se encontraron facotores no triviales!")
                   

print(QS(837209,1000,1000))    
