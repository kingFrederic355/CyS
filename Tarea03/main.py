import src.ecies as ec


#respuesta inciso 3
print('Sea la curva y^2 = x^3 + x + 1mod(29) y el punto P = (8, 12) encuentre m tal que mP = (25, 22).')
ec.getPoints(8,12,1,29)
print('Por lo que el valor de m que cumple es m=4')



#respuesta inciso 4
print('\n\nDada E(y^2 = x^3 + x + 1,(8, 12), m,(25, 22), 29)')
print('Descifre el mensaje: ((17,0),17) ((25,0),4)((12,1),5)((22,0),6)((28,1),23)((13,1),10) ((6,0),13) ((11,1),24)((19,1),13)((24,1),28)')
tarea = [[[17,0],17],[[25,0],4],[[12,1],5],[[22,0],6],[[28,1],23],[[13,1],10],[[6,0],13],[[11,1],24],[[19,1],13],[[24,1],28]]
curva = [1,1,29]
mensaje = ec.eciesDecode(tarea,curva,4)
print(mensaje)