import Hill as hl
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
option = -1
while(option != '0'):
    option = input('Que deseas hacer:\n1. Cifrar usando el Algoritmo de Hill\n2. Descifrar usando el Algoritmo de Hill\n0. Salir\n>>>  ')
    if option == '1':
        print('Cifrado de Hill')
        key = input('Ingrese la palabra clave de cifrado:\n>>>  ')
        msg = input('Ingrese el mensaje decifrar, el mensaje debe ser un texto plano, sin signos y con letras mayusculas:\n>>>  ')
        result = hl.cifradoHill(msg,key,alfabeto)
        print('Resultado: '+result+'\n')
    elif option == '2':
        print('Descifrado de Hill')
        key = input('Ingrese la palabra clave de cifrado:\n>>>  ')
        msg = input('Ingrese el mensaje descifrar, el mensaje debe ser un texto plano, sin signos y con letras mayusculas:\n>>>  ')
        result = hl.decifradoHill(msg,key,alfabeto)
        print('Resultado: '+result+'\n')