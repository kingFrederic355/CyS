from operator import index
from posixpath import split
from turtle import clear

# take second element for sort
def takeSecond(elem):
    return elem[1]

def wordCounter(cadena):
    words = cadena.split()
    noRepeatList = list(dict.fromkeys(words))
    repeat = [0] * len(noRepeatList)
    resultado = []
    for i in range(len(words)):
        repeat[noRepeatList.index(words[i])] += 1
    for i in range(len(noRepeatList)):
        resultado.append([noRepeatList[i], repeat[i]])
    return resultado

def letterCounter(cadena, alfabeto):
    repeat = [0]* len(alfabeto) #Llenamos nuestra lista de letras con 0
    resultado = [] #Incidencias de las letras
    for i in range(len(cadena)):
        try:
            # Buscamos si tenemos una letra dentro del alfabeto dado
            # En caso de que la encuentre sumamos una a las incidencias
            repeat[ alfabeto.index(cadena[i]) ] += 1
        except:
            #Ignoro el simbolo
            k = 1
    for i in range(len(alfabeto)):
        if(repeat[i] > 0): #Guardaremos una lista con todas las incidencias, en caso de que no hubiese no se anexa
            resultado.append([alfabeto[i],repeat[i]])
    return resultado


def clearText(text,alfa):
    alfaplusspace = alfa+' '
    clearMessage = ''
    for letter in range(len(text)):
        try:
            alfaplusspace.index(text[letter])
            #print(text[letter])
            clearMessage = clearMessage + text[letter]
        except:
            k = 1
    return clearMessage   

def filterSize(list,size):
    aux = []  
    for i in range(len(list)):
        if(len(list[i][0]) == size):
            aux.append(list[i])
    return aux

def maxWord(list):
    aux = 0  
    for i in range(len(list)):
        if(len(list[i][0]) > aux):
            aux = len(list[i][0]) 
    return aux
    
'''



#mensaje = clearText(mensaje,alfabeto)

palabras = wordCounter(mensaje)
palabras.sort(key=takeSecond)

rep = letterCounter(mensaje,alfabeto)
rep.sort(key=takeSecond)

oneLetter = filterSize(palabras,4)

for i in range(len(rep)):
    print('Letra: ' + rep[i][0] + ' Repeticiones: ' +  str(rep[i][1]))

for i in range(len(palabras)):
    print('Palabra: ' + palabras[i][0] + ' ------------------- Rep: ' +  str(palabras[i][1]))

for i in range(maxWord(palabras)+1):
    print('Tamaño: '+str(i))
    oneLetter = filterSize(palabras,i)

    for i in range(len(oneLetter)):
        print('Palabra: ' + oneLetter[i][0] + ' Rep: ' +  str(oneLetter[i][1]))
'''

mensaje = 'JMNCIMS JBTCJBTFAMS Y CAUBAFMKCS NFOCRCKAFBICS IB PRFJCRB PRCDUKTB QUC SURDC CS QUC CS UK JMNCIM JBTCJBTFAM CKTCKNCJMS PMR JMNCIM JBTCJBTFAM AMJM UK AMKGUKTM NC CAUBAFMKCS M RCIBAFMKCS ABPBACS NC CKJBRABR IBS ABRBATCRFSTFABS JBS PRMOUKNBS NC UK SFSTCJB AMJPICGM SC PRCTCKNC QUC CI JMNCIM SCB ABPBZ NC PRCNCAFR Y AMKTRMIBR IB CVMIUAFMK. IMS JMNCIMS SC B PIFABK CK OFSFAB, QUFJFAB, LFMIMDFB C FKDCKFCRFB BATUBIJCKTC SC FKVMIUARBK CK IBS OFKBKZBS, IB CAMIMDFB, SMAFMIMDFB, Y JUAEBS MTRBS BRCBS. PBRTCS CSCKAFBICS NC UK JMNCIM UKM ICYCS DCKCRBICS, TMNBS PRMVFCKCK NC IB JCABKFAB PMR CGCJPIM IB ICY NC IB AMKSCRVBAFMK NC IB JBSB, NC IB CKCRDFB, NCI JMJCKTM Y MTRBS. NMS RCIBAFMKCS AMKSTFTUTFVBS QUC NCPCKNC NCI OCKMJCKM QUC SC CSTUNFB, PMR CGCJPIM: IB ICY NC OMURFCR NC AMKNUAAFMK NC ABIMR, ICY NC OFAH NC NFOUSFMK Y CKTRC MTRBS. IB PRFJCRB NCOFKFAFMK QUC KCACSFTBJMS CS IB NC CAUBAFMK CK NCRFVBNB PBRAFBI CNP. NCOFKFAFMK UKM UKB CAUBAFMK NFOCRCKAFBI PBRAFBI NC IB OMRJB UKB OUKAFMK AMK IMS SFDUFCKTCS BRDUJCKTMS IBS AMMRNCKBNBS CSPBAFBIC SCDUFNBS NC UKB OUKAFMK U SCDUFNB NC IBS NCRFVBNBS PBRAFBICS NC IB OUKAFMK U SCDUK SCBK RCQUCRFNBS IBS NCRFVBNBS PBRAFIB Y CSTM FDUBIBNB B ACRM NMKNC IB OUKAFMK U NCPCKNC NC AMMRNCKBNBS CSPBAFBICS'
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mensajePrueba = 'JMNCIMS JBTCJBTFAMS Y CAUBAFMKCS NFOCRCKAFBICS'
alfabeto =           'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
palabra = 'BLANCODE'
alfabetodescifrado = 'BLANCODEFGHIJKMPQRSTUVWXYZ'

def descifra(txt,alfa,descifrado):
    clearMessage = ''
    for letter in range(len(txt)):
        try:
            #Busco el indice en el texto decifrado
            indice = descifrado.index(txt[letter])
            clearMessage = clearMessage + alfa[indice]
        except:
            clearMessage = clearMessage + txt[letter]
    return clearMessage 

print(descifra(mensaje,alfabeto,alfabetodescifrado))
    