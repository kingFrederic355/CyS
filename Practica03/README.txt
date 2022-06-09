Criptografia y Seguridad 2022-2
Lagunas Trejo, Abraham

Practica 3: Ecies simplificado

Implementacion del algoritmo de cifrado y decifrado ECIES en su version simplificada.

Esta Implementacion consta de los archivos:

Practica
    src
        app.py
        ecies.py
        main.py
        misc.py

El archivo 'misc.py' contiene funciones auxiliares para el correcto funcionamiento de los algoritmos de ecies
Por su parte 'ecies.py' contiene funciones para el calculo de puntos, suma de puntos, encriptado y desencriptado
haciendo uso de curvas elipticas

                                            C I F R A D O

El archivo 'app.py' es una Implementacion visual que facilita el uso del encriptado. En esta solo es necesario
colocar los valores que se nos soliciten, es decir A, B y P para la curva; el punto P y Q

Asi mismo, de no conocer el valor de Q; esta Implementacion nos permite calcularlo usando un valor m y el punto P dado

Por ultimo el mensaje se coloca en la seccion de 'Mensaje sin decifrar' y se debe dar click en cifrar

NOTA: el correcto funcionamiento de este dependera de la curva y el orden de esta misma, por lo que es recomendable usar curvas
que se encuentran en las notas

Asi mismo el cifrado se puede hacer usando unicamente la terminal con el archivo 'main.py' en el cual todos los elementos cuentan
con comentarios para hacer el encriptado

                                        D E S C I F R A D O

Para hacer el desencriptado solo se podra realizar usando el archivo 'main.py' debido a problemas con el casteo de los mensajes cifrados

Para descifrar se deberan modificar los valores del archivo y colocar el texto cifrado, el cual debe de ser una lista de la forma
mensaje = [[[x1,y1],z1],[[x2,y2],z2], ... , [[xn,yn],zn]]


Queda prohibido su uso para fines lucrativos, UNAM, Facultad de Ciencias 2022