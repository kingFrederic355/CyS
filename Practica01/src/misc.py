# Abraham Lagunas Trejo

# Criptografia y seguridad 2022-2

# Archivo con utilidades para la parctica 1

#Funcion que genera una tabla de Vignare dado un alfabeto dado
def vignareTable(alpha):
    tabla = []
    for i in range(len(alpha)):
        tabla.append([])
        for j in range(len(alpha)):
            tabla[i].append(alpha[(i+j)%len(alpha)] )
    return tabla

#Funcion para visualizar la tabla de Viganere dada
def tableToString(table): 
    texto = ''
    for i in range(len(table)):
        texto += ' '
        for j in range(len(table)):
            texto += '----'
        texto += '\n'
        texto += '| '
        
        for j in range(len(table)):
            texto += table[i][j] + ' | '
        texto += '\n'
    return texto

'''
Funcion que hace el cifrado de viganare
- message: Mensaje que queremos cifrar
- key: Palabra clave de cifrado
- alfa: Alfabeto en el cual esta cifrado el mensaje
'''
def cifrarMensaje(message,key,alfa):
    vignare = vignareTable(alfa) #Tabla de vignare correspondiente)
    cifrado = '' #En esta variable guardaremos el mensaje cifrado
    for letter in range(len(message)):
        i = alfa.index(message[letter]) # Indice dado por el mensaje
        j= alfa.index(key[letter%len(key)]) # Indice dado por la clave
        cifrado += vignare[i][j] # Letra correspondiente en la tabla
    return cifrado
'''
Funcion que hace el descifrado de viganare
- message: Mensaje que queremos descifrar
- key: Palabra clave de cifrado
- alfa: Alfabeto en el cual esta descifrado el mensaje
'''
def decifraMensaje(text,key,alfa):
    tabla = vignareTable(alfa) #Tabla de vignare correspondiente
    mensaje = ''
    for i in range(len(text)):
        letterPos = alfa.index(key[i%len(key)]) # Posicion de la letra de la clave
        letterNumber = tabla[letterPos].index(text[i]) # Indice en el cual se cuencuetra la letra en base al renglon
        mensaje += alfa[letterNumber] #Letra correspondiente a la letra correcta
    return mensaje