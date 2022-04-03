Abraham Lagunas Trejo

Programa para decifrado de Vignare y Hill

Para el correcto uso de este programa se cuentan con 2 formas de ejecucion.

- Usando la terminal
- Usando una app

En caso de querer usar cualquiera de las dos implementaciones de los algoritmos solo basta con escribir 
en la terminal:

$ python3 <algoritmo><forma>.py 

Ejemplo:

$ python3 viganereApp.py 

Para el correcto uso de las versiones como app se deben instalar los siguientes paquetes

apt-get install python3-tk
apt install python3-pip
python3 -m pip install PySimpleGUI Pillow

Esta implementacion cuenta con un alfabeto de 27 letras para Viganere y uno de 26 letras para Hill, esto es dado a que se estuvieron probando multiples cifrados con hill pero las inversas no correspondian.
El caso donde esto no parecia salir mal era cuando la palabra clave era DDCF