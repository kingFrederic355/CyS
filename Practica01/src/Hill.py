import math
import matrix as mx

"""
Funcion que aplica el algoritmo de hill.

Args:
    txt: Texto plano a cifrar.
    clave: Palabra clave que usaremos para cifrar
    alfa: alfabeto que usaremos en nuestro cifrado

Returns:
    Regresa la cadena ya cifrada por el algoritmo
"""
def cifradoHill(txt,clave,alfa):
    #Paso 1, verificar que la palabra clave sea potencia de 2 o 3
    n = len(clave)
    if (n == 4 or n == 9):
        
        n = (int)(math.sqrt(n))
        claveAmatrix = mx.txt2num(clave,alfa) # Convertimos la clave en sus valores numericos
        claveAmatrix = mx.lst2vtr(claveAmatrix,n) #La convertimos en vectores de la cardinalidad raiz de la longitud
        claveAmatrix = mx.lst2vtr(claveAmatrix,n) # Finalmente obtenemos la matriz de decifrado
        claveAmatrix = claveAmatrix[0]
        
        det = 0
        if n == 2:
            det = mx.det2x2(claveAmatrix)
        else:
            det = mx.det3x3(claveAmatrix)
        print(det)

        if det%len(alfa) == 0:
            print('La palabra ingresada no cuenta con inversa, por favor ingrese una palabra valida')
        else:
            textoAVector = mx.txt2num(txt,alfa) #Convertimos el texto en sus valores numericos
            textoAVector = mx.lst2vtr(textoAVector,n) # Los transformamos en vectores de la misma cardinalidad
            # Como no podemos asegurarnos que todos los textos que ingresemos sean de una cardinalidad igual a la raiz de la palabra
            # procederemos a revisar el ultimo elemento en la lista de vectores del texto.
            # Si el ultimo vector es de menor cardinalidad lo llenaremos de 0s
            mx.fillVector(textoAVector,n)
            txtCifrado = mx.mtrx4vctrs(claveAmatrix,textoAVector)
            final = []
            for i in range(len(txtCifrado)):
                final.append(mx.vectorModulo(txtCifrado[i],len(alfa)))            
            final = mx.vtr2lst(final)
            final = mx.num2txt(final,alfa)
            return final
    else:
        print('Palabra no valida')

def decifradoHill(txt,clave,alfa):
    #Paso 1, verificar que la palabra clave sea potencia de 2 o 3
    n = len(clave)
    if (n == 4 or n == 9):
        
        n = (int)(math.sqrt(n))
        claveAmatrix = mx.txt2num(clave,alfa) # Convertimos la clave en sus valores numericos
        claveAmatrix = mx.lst2vtr(claveAmatrix,n) #La convertimos en vectores de la cardinalidad raiz de la longitud
        claveAmatrix = mx.lst2vtr(claveAmatrix,n) # Finalmente obtenemos la matriz de decifrado
        claveAmatrix = claveAmatrix[0]
        inversa = []
        if n == 2:
            inversa = mx.inversa2x2(claveAmatrix,len(alfa))
        else:
            inversa = mx.inversa3x3(claveAmatrix,len(alfa)) 
        textoAVector = mx.txt2num(txt,alfa) #Convertimos el texto en sus valores numericos
        textoAVector = mx.lst2vtr(textoAVector,n) # Los transformamos en vectores de la misma cardinalidad
        txtDecode = mx.mtrx4vctrs(inversa,textoAVector)
        final = []
        for i in range(len(txtDecode)):
            final.append(mx.vectorModulo(txtDecode[i],len(alfa)))
        final = mx.vtr2lst(final)
        final = mx.num2txt(final,alfa)
        return final
    else:
        print('Palabra no valida')