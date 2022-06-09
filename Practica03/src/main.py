import ecies as ec

# Curva eliptica a utilizar
# curva se describe como curva = [A,B,P]
# Donde A y B son los valores de la curva x^3 + Ax + B y P es el campo a usar 
curva = [1,14,31]

# p es un punto P que pasa sobre la curva ingresada
p = [8,21]

# valor m
m = 8

# punto Q el cual se tiene que Q = mP
q = ec.getSuma(p[0],p[1],curva[2],curva[0],m)

# El mensaje a cifrar se puede modificar desde aqui
mensajeACifrar = 'BIENVENUTIACASA'

encoded = ec.encode(curva,p,q,30,mensajeACifrar)
print('Mensaje encriptado: ' + str(encoded))

# Mensaje a decifrar
# El mensaje debe ser de la forma 'mensaje = [[[x1,y1],z1],[[x2,y2],z2], ... , [[xn,yn],zn]]'
mensajeCifrado = [[[24, 1], 13], [[1, 0], 7], [[8, 1], 5], [[20, 1], 8], [[24, 1], 19], 
[[9, 1], 30], [[27, 1], 25], [[27, 1], 22], [[15, 0], 21], [[25, 0], 16], [[29, 1], 24], 
[[25, 1], 26], [[20, 1], 5], [[19, 0], 10], [[29, 1], 24]]

mensaje = ec.eciesDecode(mensajeCifrado,curva,m)
print('Mensaje desencriptado: '+mensaje)