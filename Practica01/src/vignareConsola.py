# Abraham Lagunas Trejo

# Criptografia y seguridad 2022-2

# Cifrado de Vignare y Hill
from operator import mod
import time
import misc as ms

#Variable para simular que el proceso tarda
waitTime = 3

'''
 Alfabeto que tendra nuestro cifrado
 En este caso se tiene el alfabeto español, por lo cual se tienen 27 letras para los indices
'''
spanishAlphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

#Mensaje que queremos cifrar
plaintext = ''
key = ''

option = ''
while(option != '0'):
    
    option = input('\nQue quieres hacer:  \n 1. Cifrar un mensaje \n 2. Descifrar un mensaje \n 0. salir \n >>> ')
    if(option == '0'):
        print("Gracias por usar este software")
    
    #Cifrado de mensajes    
    elif(option == '1'):
        plaintext = input('Ingresa tu mensaje con todas las letras mayusculas y sin espacios:\n >>> ')
        key = input('Ingresa la clave con todas las letras mayusculas y sin espacios:\n >>> ')
        print('Cifrando mensaje')
        time.sleep(waitTime)
        print('Mensaje cifrado: \n')
        print(ms.cifrarMensaje(plaintext,key,spanishAlphabet))
        time.sleep(waitTime)
    #Descifrado de mensajes    
    elif(option == '2'):
        decript = input('Ingresa el mensaje a decifrar:\n >>> ')
        key = input('Ingresa la clave de decifrado:\n >>> ')
        print('Decifrando mensaje')
        time.sleep(waitTime)
        print('Mensaje decifrado: \n')
        print(ms.decifraMensaje(decript,key,spanishAlphabet))
        time.sleep(waitTime)
    else:
        print('Opcion no valida, vuelve a intentarlo')
    
