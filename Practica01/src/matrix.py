"""
Funcion para convertir una cadena de leras en una lista con sus respectivos valores en un alfabeto dado.

Args:
    txt: El texto que queremos manipular.
    alfa: Alfabeto del cual obtendremos los valores de cada letra.

Returns:
    Regresa una lista con los valores numericos correspondientes a cada letra.
"""
from unittest import result


def txt2num(txt,alfa):
    result = []
    for i in range(len(txt)):
        result.append(alfa.index(txt[i]))
    return result

"""
Funcion para convertir una cadena de numeros en una palabra usando un alfabeto dado.

Args:
    list: Valores numericos correspondientes a las letras.
    alfa: Alfabeto que usaremos.

Returns:
    Regresa una cadena con las letras.
"""
def num2txt(list,alfa):
    result = ''
    for i in range(len(list)):
        result += alfa[list[i]]
    return result

"""
Funcion para convertir una lista en un arreglo de vectores.

Args:
    lst: Lista con valores, pueden ser numericos o de otro tipo.
    size: Tamaño del vector.

Returns:
    Regresa una lista con vectores de tamaño n.
"""
def lst2vtr(lst,size):
    vtrs = []
    for i in range(0,len(lst),size):
        part = []
        for j in range(size):
            if(i+j < len(lst)):
                part.append(lst[i+j])
        vtrs.append(part)
    return vtrs

def vtr2lst(lst):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            result.append(lst[i][j])
    return result

"""
Funcion para rellenar de 0 el ultimo vector en caso de que este no tenga el tamaño indicado.

Args:
    vctr: Lista de vectores.
    size: Tamaño que debe tener cada vector.
"""
def fillVector(vctr, size):
    tamanio = len(vctr[len(vctr)-1])
    if(tamanio< size):
        for i in range(size - tamanio):
            vctr[len(vctr)-1].append(0)

"""
Funcion para multiplicar una matriz por un numero.

Args:
    mtrx: Matriz a multiplicar.
    num: valor a multiplicar.

Returns:
    Regresa una matriz cuyos elementos son multiplicados por n.
"""
def mtrx4num(mtrx, num):
    result = []
    for i in range(len(mtrx)):
        renglon = []
        for j in range(len(mtrx[i])):
            renglon.append(0)
        result.append(renglon)
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            result[i][j] = mtrx[i][j]*num
    return result

"""
Funcion para multiplicar una matriz de k * K  por un vector de tamanio k * 1.

Args:
    mtrx: Matriz a multiplicar.
    vctr: Vector a multiplicar.

Returns:
    Regresa el vector multiplicado por la matriz.
"""
def mtrx4vctr(mtrx,vctr):
    result = []
    n = len(vctr)
    for i in range(n):
        value = 0
        for j in range(n):
            value += mtrx[i][j]*vctr[j]
        result.append(value) 
    return result

"""
Funcion para multiplicar una matriz de k * K  por un multiples vecotres de tamanio k * 1.

Args:
    mtrx: Matriz a multiplicar.
    vctrs: Vectores a multiplicar.

Returns:
    Regresa una lista con vectores multiplicados por la matriz.
"""
def mtrx4vctrs(mtrx,vtrs):
    result =  []
    for i in range(len(vtrs)):
        result.append(mtrx4vctr(mtrx,vtrs[i]))
    return result

"""
Funcion que evalua todos los valores en un vector y los convierte en su respetivo valor usando el modulo n.

Args:
    vctr: Vector a sacar modulo.
    mod: Valor que tendra el modulo.

Returns:
    Regresa el vector en base al modulo
"""
def vectorModulo(vctr, mod):
    resultado = []
    for i in range(len(vctr)):
        vctr[i] = vctr[i] % mod
        resultado.append(vctr[i])
    return resultado

"""
Funcion para evaluar los elementos en una matriz y obtener su equvalente en base al modulo dado.

Args:
    mtrx: Matriz a evaluar.
    mod: Valor del modulo.

Returns:
    Una matrix modulo m
"""
def MatrizModulo(mtrx, mod):
    resultado = []
    for i in range(len(mtrx)):
        renglon = []
        for j in range(len(mtrx)):
            renglon.append(mtrx[i][j]%mod)
        resultado.append(renglon)
    return resultado

"""
Funcion que multiplica todos los valores de una lista de vectores por una matriz de la misma cardinalidad.

Args:
    lstVctr: Lista de vectores a multiplicar.
    keyMtrx: Matriz que multiplicara a cada vector.

Returns:
    Regresa los vectores ya ultiplicados por la matriz
"""
def procesa(lstVctr,keyMtrx):
    result = []
    for i in range(len(lstVctr)):
        multiplicacion = mtrx4vctr(keyMtrx,lstVctr[i])
        modulo = vectorModulo(multiplicacion,len(alfabeto))
        result.append(modulo)
    return result
"""
Funcion que devuelve el determinante de una matriz de tamaño 2 x 2.

Args:
    mtrx: Matriz a la que se le desea sacar el determinante.

Returns:
    Determinante de la matriz
"""
def det2x2(mtrx):
    return mtrx[0][0]*mtrx[1][1] - mtrx[0][1]*mtrx[1][0]

"""
Funcion que devuelve el determinante de una matriz de tamaño 3 x 3.

Args:
    mtrx: Matriz a la que se le desea sacar el determinante.

Returns:
    Determinante de la matriz
"""
def det3x3(mtrx):
    result=mtrx[0][0]*mtrx[1][1]*mtrx[2][2] + mtrx[1][0]*mtrx[2][1]*mtrx[0][2] +mtrx[2][0]*mtrx[0][1]*mtrx[1][2]
    result=result+(mtrx[0][2]*mtrx[1][1]*mtrx[2][0])*-1 + (mtrx[1][2]*mtrx[2][1]*mtrx[0][0])*-1 + (mtrx[2][2]*mtrx[0][1]*mtrx[1][0])*-1
    return result
"""
Algoritmo extendido de euclides.

Args:
    a: Primer valor a comparar.
    b: Segundo valor a comparar.

Returns:
    Un arreglo con los valores del mcd, el inverso de a y el inverso de b
"""
def eucExt(a,b):
    r = [a,b]
    s = [1,0] 
    t = [0,1]
    i = 1 
    q = [[]]
    while (r[i] != 0): 
        q = q + [r[i-1] // r[i]]
        r = r + [r[i-1] % r[i]]
        s = s + [s[i-1] - q[i]*s[i]]
        t = t + [t[i-1] - q[i]*t[i]]
        i = i+1
    return (r[i-1], s[i-1], t[i-1])
"""
Funcion para obtener la sub matriz dados los valores i, j de la matriz dada.

Args:
    mtrx: Matriz original.
    k: Renglon de la matriz
    l: columna de la matriz

Returns:
    Matriz de tamaño mtrx-1
"""
def getMtxr(mtrx,k,l):
    result = []
    for i in range(len(mtrx)):
        if i!=k:
            renglon = []
            for j in range(len(mtrx[i])):
                if(j != l):
                    renglon.append(mtrx[i][j])
            result.append(renglon)
    return result

"""
Funcion para obtener la matriz adjunta.

Args:
    mtrx: Matriz original.
Returns:
    Matriz adjunta de mtrx
"""
def adjunta3x3(mtrx):
    adj = []
    for i in range(len(mtrx)):
        renglon = []
        for j in range(len(mtrx)):
            renglon.append(det2x2(getMtxr(mtrx,i,j))*(-1)**(i+j))
        adj.append(renglon)
    return adj

"""
Funcion para obtener la inversa de una matriz de 2 x 2.

Args:
    mtrx: Matriz de la cual queremos obtener su inversa.
    mod: Modulo sobre el cual vamos a trabajar.

Returns:
    Matriz de 2 x 2 correspondiente a la inversa de mtrx
"""
def inversa2x2(mtrx,mod):
    det = det2x2(mtrx)
    det = eucExt(det,mod)[1] #Esto ya que el inverso para el determinante esta en el segundo elemento del arreglo
    trans = [[mtrx[1][1],(-1)*mtrx[0][1]],[mtrx[1][0]*(-1),mtrx[0][0]]]
    trans = MatrizModulo(trans,mod)
    inversa = mtrx4num(trans,det)
    inversa = MatrizModulo(inversa,mod)
    return inversa

"""
Funcion para obtener la inversa de una matriz de 3 x 3.

Args:
    mtrx: Matriz de la cual queremos obtener su inversa.
    mod: Modulo sobre el cual vamos a trabajar.

Returns:
    Matriz de 2 x 2 correspondiente a la inversa de mtrx
"""
def inversa3x3(mtrx,mod):
    det = det3x3(mtrx)
    det = eucExt(det,mod)[1] #Esto ya que el inverso para el determinante esta en el segundo elemento del arreglo
    adj = adjunta3x3(mtrx)
    adj = MatrizModulo(adj,mod)
    inversa = mtrx4num(adj,det)
    inversa = MatrizModulo(inversa,mod)
    return inversa