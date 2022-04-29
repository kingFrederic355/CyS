from traceback import print_tb
import misc as ms
import time

def generaClaves():
    # Primera parte, obtener n

    # Primero obtendremos 2 valores p y q de tamaño 100
    p = ms.getPrime()
    q = ms.getPrime()
    '''# Debug
    print("valor p:\n"+str(p)+
        "\nvalor q:\n"+str(q))'''
    n = p*q
    time.sleep(3)
    print('Valor de n:\n'+str(n))
    # Segunda parte , obtener e

    # Usando p y q generaremos phi
    phi = ms.euler(p,q)

    # Calcularemos e tal que, mcd(e,phi) = 1, es decir, e sea coprimo de phi
    e = ms.getCoPrime(phi)
    time.sleep(3)
    print('Valor de e:\n'+str(e))

    # Tercera parte, obtener el inverso de e, mejor conocido como d
    d = ms.modInverse(e,phi)
    time.sleep(3)
    print('Valor de d:\n'+str(d))
    print(str(e*d % phi))


# Funcion de encriptado de RSA la cual toma un mensaje m y la transforma usando la operacion c ≅ m^e mod n
def encrypt(m,e,n):
    ascii = ms.string2ASCII(m)
    msg = []
    for letter in ascii:
        msg.append(ms.power(letter,e,n))
    final = ''
    for eltr in msg:
        final += str(eltr) +'3550209'

    return final

def decrypt(m,d,n):
    num = m.split('3550209')
    num = num[0:len(num)-1]
    
    for i in range(len(num)):
        num[i] = int(num[i])

    dmsg = []
    for ltr in num:
        dmsg.append(ms.power(ltr,d,n))
    mensaje = ''
    for num in dmsg:
        mensaje += chr(num)
    return mensaje



option = ''
while(option != '0'):
    option = input("1. Genera claves\n2. Encripta mensaje\n3. Desencripta mensaje\n0. Salir\n>> ")
    if option == '0':
        print("Gracias por usar el programa")
    elif option == '1':
        generaClaves()
    elif option == '2':
        msg = input("Ingresa tu mensaje:\n")
        n = int(input("Ingresa tu valor n:\n"))
        e = int(input("Ingresa tu valor e:\n"))
        print(encrypt(msg,e,n))
    elif option == '3':
        msg = input("Ingresa tu mensaje:\n")
        n = int(input("Ingresa tu valor n:\n"))
        d = int(input("Ingresa tu valor d:\n"))
        print(decrypt(msg,d,n))
    else:
        print("Ingrese una opcion valida")
