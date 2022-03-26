textoCifrado =    ['JV', 'AX', 'SO', 'PN', 'PT', 'MR', 'YT', 'DW', 'EE', 'YM', 'GC', 'MR', 'JR', 'RN', 'WC', 'LB', 'JV', 'DF', 'FP','MK']
#textoCifrado =    ['JV', 'AK', 'SO', 'PN', 'PT', 'ME', 'YG', 'DJ', 'EE', 'YM', 'GC', 'ME', 'JR', 'RN', 'WC', 'LB', 'JV', 'DF', 'FP','MK']

textoDescifrado = ['EL', 'PO', 'SO', 'ER', 'AP', 'RO', 'FU', 'ND', 'OY', 'OS', 'CU', 'RO', 'YV', 'IV', 'IA', 'EN', 'EL', 'UN', 'AF', 'AM']
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Matriz = ['GB','KD']

'''
for i in range(len(textoCifrado)):
    p = alfabeto.index(textoCifrado[i][0])
    q = alfabeto.index(textoCifrado[i][1])
    a = alfabeto.index(textoDescifrado[i][0])
    b = alfabeto.index(textoDescifrado[i][1])
    print('a*'+alfabeto[p]+' b*'+alfabeto[q]+ '= a*'+ str(p) +' + b*'+ str(q) +' = ' + str(a))    
    print('c*'+alfabeto[p]+' d*'+alfabeto[q]+ '= c*'+ str(p) +' + d*'+ str(q) +' = ' + str(b)+'\n')
'''

'''
for i in range(26):
    result = (i*5)%26
    print('Numero: ' +str(i)+ ' resultado: '+ str(result))'''


'''
for i in range(len(textoDescifrado)):
    p = alfabeto.index(textoDescifrado[i][0])
    q = alfabeto.index(textoDescifrado[i][1])
    a = alfabeto.index(Matriz[0][0])
    b = alfabeto.index(Matriz[0][1]) 
    c = alfabeto.index(Matriz[1][0]) 
    d = alfabeto.index(Matriz[1][1]) 
    print('a*'+alfabeto[p]+' b*'+alfabeto[q]+ '= a*'+ str(p) +' + b*'+ str(q) +' = ' + str(p) + )    
    print('c*'+alfabeto[p]+' d*'+alfabeto[q]+ '= c*'+ str(p) +' + d*'+ str(q) +' = ' + str(q)+'\n')
    indx1 = (a*p + b*q) % 26
    indx2 = (c*p + d*q) % 26
    
    #print(alfabeto[indx1]+alfabeto[indx2])
'''


matrizDes = ['PV','CE']
for i in range(len(textoCifrado)):
    p = alfabeto.index(textoCifrado[i][0])
    q = alfabeto.index(textoCifrado[i][1])
    a = alfabeto.index(matrizDes[0][0])
    b = alfabeto.index(matrizDes[0][1]) 
    c = alfabeto.index(matrizDes[1][0]) 
    d = alfabeto.index(matrizDes[1][1]) 
    
    
    indx1 = (a*p + b*q) % 26
    indx2 = (c*p + d*q) % 26
    
    print(alfabeto[indx1]+alfabeto[indx2])
