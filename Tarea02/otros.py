# Firma digital RSA
n = 837209
a = 803021
b = 358481

# key = {n,p,q,e,d}
# Se define la firma como la funcion
# S(k) = x^a mod n = y
#
# Para corroborar que la firma corresponda, lo que se hace es 
#
# x cong y^b mod n}

# En este caso 
x = 406281
y = pow(x,a,n)
print(y)
f1 = 759181
f2 = 489650

f1decode = pow(f1,b,n)
f2decode = pow(f2,b,n)

print('La firma: '+str(f1)+' corresponde con x?\n'+str(x == f1decode)+' Valor de F1:'+str(f1decode))
print('La firma: '+str(f2)+' corresponde con x?\n'+str(x == f2decode)+' Valor de F2:'+str(f2decode))