# Pruebas de primalidad 
from math import sqrt

def raiz(n):
    # Primero revisamos que el numero ingresado sea mayor a 2
    if n < 2:
        print( "El número es menor que 2" )
        exit()
    # Corroboramos si es 2, ya que como sabemos el 2 es el unico primo par
    elif n == 2:
        print( "El número es primo" )
        exit()
    # Revisamos que el numero no sea par
    elif n % 2 == 0:
        print( "El número no es primo, es divisible por 2" )
        exit()
    # Si no cumple con ninguna de las condiciones lo que haremos sera lo siguiente
    
    else:
        i = 3
        x = int(sqrt(n))
        for i in range(3, int(sqrt(n)), 2):# Tomaremos el rango desde 3 hasta el valor entero de la raiz de n 
            if n % i == 0: # Usaremos la variable i para revisar todos y cada uno de los numeros del rango de arriba
                print( "El número no es primo, es divisible por: " , i ) # Si el residuo de n modulo i es igual a 0 entonces i es el divisor de n
                exit()

        print(n, "es un número primo" )

# Teorema de Fermat
def fermat(n,t = -1):
    if(t==-1): # En caso de que solo se nos de un valor n, asiganaremos a t como el mismo valor n
        t = n
    for i in range(1,t,2):
        residuo = pow(i,n-1,n)
        print(i) 
        if(residuo != 1):
            print('No es primo, el valor que divide es: '+str(i))
            exit()
    print('Despues de '+str(t)+' iteraciones no se ha encontrado un divisor de '+str(n))


n1 = 67891234321234567897
n2 = 13579246809876879657
n3 = 23192157311717657191

# Prueba usando raiz de n
# raiz(n1)
# raiz(n2)

# Prueba de fermat para n3
#fermat(23192157311717657191,10000000)