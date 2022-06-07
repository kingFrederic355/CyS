from cmath import sqrt
from numpy import append
import src.misc as ms
import secrets as sc

"""
Funcion para calcular el valor de lambda

Args:
    x1:     valor x del primer punto
    y1:     valor y del primer punto
    x2:     valor x del segundo punto
    y2:     valor y del segundo punto
    mod:    modulo o campo sobre el cual se mantendran los valores
    a:      valor a de la curva

Returns:
    valor lambda correspondiente para la suma"""

def getLambda(x1,y1,x2,y2,mod,a):
    divisor = 1
    dividendo = 1
    # Si P = Q 
    if(x1 == x2):
        divisor = (2*y1) % mod
        dividendo = (3*x1*x1 + a) % mod
    else:
        divisor = (x2 - x1)  % mod
        dividendo = (y2 - y1)  % mod
    divisor = ms.modInverse(divisor,mod)
    if divisor == -1:
        print('lambda no encontrada')
        return -1
    return (dividendo*divisor) % mod

"""
Funcion para sumar 2 puntos de una curva eliptica

Args:
    x1:     valor x del primer punto
    y1:     valor y del primer punto
    x2:     valor x del segundo punto
    y2:     valor y del segundo punto
    a:      valor a de la curva
    mod:    modulo o campo sobre el cual se mantendran los valores

Returns:
    Una lista con el punto [x3,y3]"""
def sumaPuntos(x1,y1,x2,y2,a,mod):

    # Suma de infinito
    if(x1 == 0 and y1 == 0):
        return[x2,y2]

    if(x2 == 0 and y2 == 0):
        return[x1,y1]
    # Suma de inversos, punto al infinito
    if(x1 == x2 ) and (y1 == mod - y2):
        return([0,0])


    lamb = getLambda(x1,y1,x2,y2,mod,a)
    if lamb == -1:
        return -1
    x = (lamb*lamb - x1 - x2) % mod
    y = (lamb*(x1-x) - y1) % mod
    #print(lamb,x,y)
    return [x,y]

"""
funcion recursiva para obtener la k esima suma de un punto dado

Args:
    x:      valor x del punto dado
    y:      valor y del punto dado
    mod:    modulo o campo sobre el cual se mantendran los valores
    a:      valor a de la curva
    k:      Iteracion de la cual queremos

Returns:
    Una lista con el punto [x3,y3]"""

def getSuma(x,y,mod,a,k):
    q = [0,0]
    p = [x,y]
    klist = ms.binaryList(k)
    for i in klist:
        if i:
            q = sumaPuntos(p[0],p[1],q[0],q[1],a,mod)
        p = sumaPuntos(p[0],p[1],p[0],p[1],a,mod)
    return q

"""
Funcion que comprime un punto

Args:
    x:      valor x del punto dado
    y:      valor y del punto dado
    
Returns:
    [x,y mod 2]"""
def zipPoint(x,y):
    return [x,y%2]

"""
Funcion que descomprime un punto 

Args:
    x:      valor x del punto dado
    y:      valor y del punto dado
    a:      Valor A de la curva
    b:      Valor B de la curva
    m:      Modulo o campo de la curva
    
Returns:
    Punto [x,y] tal que y = z^(p+1)/4 mod m

NOTA: esta descomprension solo funciona si m = 4k + 3
"""
'''
def unzipPoint(x,y,a,b,m):
    z = (pow(x,3) + a*x + b) % m
    resultado = int((m+1)/4)
    y1 = int(pow(z,resultado ,m))
    if((y1%2)== y):
        return [x,y1]
    else:
        return [x,m-y1]'''

def unzipPoint(x,y,a,b,m):
    z = (pow(x,3) + a*x + b) % m
    result = 0
    for i in range(m):
        j = (i*i) % m
        if j == z:
            result = i
    if (result % 2 == y):
        return [x,result]
    else:
        return [x,m-result]

"""
Funcion que descifra un valor del mensaje dado

Args:
    x:      valor x comprimido
    y:      valor y comprimido
    val:    <complete>
    a:      valor a de la curva
    b:      valor b de la curva
    m:      campo para los valores de la curva
    pley:   valor de la llave publica
    
Returns:
    Valor numerico que corresponde a una letra del alfabeto dado
"""

def decodeEciesPoint(x,y,val,a,b,m,pkey):
    # Primero descomprimimos nuestro punto (x,y)
    unzip = unzipPoint(x,y,a,b,m)
    # Multiplicamos por el valor de la llave publica
    newval = getSuma(unzip[0],unzip[1],m,a,pkey)
    # Calculamos el valor decifrado
    decode = (val*(ms.modInverse(newval[0],m))) % m
    return decode

"""
Funcion que decifra un mensaje dado haciendo uso de ECIES

Args:
    encrypMsg:      Este corresponde al mensaje que se quiere desencriptar.
                    El mensaje debe tener el formato [[[x1,y1],k1],[[x2,y2],k2], ... [[xn,yn],kn]] 
    curve:          Curva usada para encriptar el mensaje
                    La curva debe estar en la forma: [a,b,m], donde a y b son los valores de la curva x^3 + ax + b y m es el valor del campo
    pkey:           Valor de la llave publica
    alphabet:       Alfabeto a usar para la desencriptacion
    
Returns:
    Cadena con el mensaje decifrado
"""
def eciesDecode(encrypMsg,curve,pkey,alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    #decodems = []
    decodems = ''
    for i in encrypMsg:
        num = decodeEciesPoint(i[0][0],i[0][1],i[1],curve[0],curve[1],curve[2],pkey)
        decodems += alphabet[(num)% len(alphabet)]
        #decodems.append(num)
    return decodems

def encodeEcies(curva,p,q,n,x):
    #Tomamos un numero random entre 1 y n
    k = sc.randbelow(n)
    if k == 0: k = 1
    kp = getSuma(p[0],p[1],curva[2],curva[0],k)
    kq = getSuma(q[0],q[1],curva[2],curva[0],k)
    y1 = zipPoint(kp[0],kp[1])
    y2 = (x*kq[0]) % curva[2]
    return [y1,y2]

def encode(curva,p,q,n,msg,alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    encodeMSG = []
    for i in msg:
        x = alphabet.index(i) +1
        encodeMSG.append(encodeEcies(curva,p,q,n,x))
    return encodeMSG

def getPoints(x,y,a,mod):
    init = [x,y]
    punto = [x,y]
    count = 1
    puntos = [punto]
    while(punto != [0,0]):
        print(str(count)+'('+str(init[0])+','+str(init[1])+') = ('+str(punto[0])+','+str(punto[1])+')')
        punto = sumaPuntos(init[0],init[1],punto[0],punto[1],a,mod)
        puntos.append(punto)
        count += 1
    print(str(count)+'('+str(init[0])+','+str(init[1])+') = (0,0)')
    return puntos
