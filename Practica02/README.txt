Abraham Lagunas Trejo

Cifrado y Descifrado de RSA

Para el correcto uso de este programa se cuentan con 2 formas de ejecucion.

- Usando la terminal
- Usando una app

Para el uso de la forma en terminal en el archivo rsa.py basta con descomentar la ultima parte del codigo

Para el uso en forma de aplicacion ejecutar el siguiente comando en la carpeta de src

$ python3 app.py 


Para el correcto uso de las versiones como app se deben instalar los siguientes paquetes

apt-get install python3-tk
apt install python3-pip
python3 -m pip install PySimpleGUI Pillow

En forma de terminal el programa es muy explicito con respecto a los datos

1. Genera claves
2. Encripta mensaje
3. Desencripta mensaje
0. Salir

Al dar click en la opcion 1, el programa nos mostrara la siguiente informacion

Ejemplo:

	Valor de n:
	<num> El cual es el producto de dos primos de 100 cifras
	Valor de e:
	<num> Valor coprimo usando el valor phi(n)
	Valor de d:
	<num> Valor que corresponde a la inversa de e

La opcion 2 nos permite encriptar un mensaje usando valores n y e dados

Ejemplo:

	Ingresa tu mensaje:
	<Mensaje que acepta mayusculas y minusculas>
	Ingresa tu valor n:
	<valor n>
	Ingresa tu valor e:
	<valor e>
	<resultado>

El mensaje encriptado es una cadena de numeros la cual solo se podra desencriptar en este programa ya que 
la separacion de letras sera dada por los numeros 3550209

Por ultimo la opcion 3 desencripta el mensaje con el formato indicado arriba

Ejemplo:

	Ingresa tu mensaje:
	<Mensaje>
	Ingresa tu valor n:
	<valor n>
	Ingresa tu valor d:
	<valor d>
	<resultado>


En caso de que se use la version como app se mostrara un menu con 5 botones.

Genera claves: Esta opcion llena los campos n,e y d haciendo uso de los mismos metodos que rsa.py

Limpia claves: Borra los campos n,e y d

Encrypta: Haciendo uso de los valores n y e de los campos del mismo nombre, toma el texto ingresado en el
campo debajo del texto 'Mensaje sin cifrar' y hace uso del algoritmo de RSA y el resultado lo muestra en el 
campo inferior

Desencrypta: De forma similar que Encrypta; se toman los valores de los campo n y d, se toma el texto del 
campo 'Mensaje cifrado' y el resultado se coloca en el campo por encima de este

Limpia: Borra el contenido de los campos de mensaje