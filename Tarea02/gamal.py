#gamal (p = 977, alpha = 53, alpha^a = 13)
# orden n = 976
# beta = 13
# Elevar alpha sobre cada potencia desde 1 hasta p

#Valores dados del cifrado


from numpy import sort


p = 229
alpha = 6
alphaa = 13

s = [2, 3, 5, 7, 11]

rep = [0, 0, 0, 0, 0]


index = []



# Buscaremos los indices de cada uno de los numeros desde 1 hasta p
for contador in range(1,p):
# Asignamos el valor de number al del contador
    number = pow(alpha,contador,p)
    copy = number
    i = 0
    while (number != 1):
        # Si el residuo es 0, quiere decir que el numero es divisible por la base, por lo cual se deja el cociente y aumentamos en uno 
        if(i >= len(s)):
                #print('El valor: ' +str(number)+' no puede dividirse usando la base ingresada')
                rep = [-1, -1, -1, -1, -1]
                break

        elif (number % s[i] == 0):
            number = number/s[i]
            rep[i] += 1
        else:
            i += 1
    #print(contador)
    index.append([copy,rep])
    rep = [0, 0, 0, 0, 0]


clearList = []
for i in index:
    if(i[1] != [-1, -1, -1, -1, -1] and i[1] != [0, 0, 0, 0, 0]):
        clearList.append(i)
 
# using list comprehension + enumerate()
# to remove duplicated 
# from list 
#clearList.sort()

for i in clearList:
    print(i)

print(len(clearList))
