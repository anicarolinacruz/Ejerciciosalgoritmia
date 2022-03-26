from ast import If, While


palabra=input("ingrese palabra: ")
totalCaracteres=len(palabra)
#vocales= a, e, i, o, u
countVocales = 0
i = 0
print (totalCaracteres)
while i <= totalCaracteres:
    print("Entro al while");
    if palabra[i] == "a":
        print("Entro al if");
        countVocales += 1;
        
    
    i +=1;
    print("Cambio contador a ", i);
else:
    print("El total de vocales son: " + countVocales);    



    





'''
While i <= totalCaracteres:
    
    print("")
    i++;
    else:
        print("")
        
'''