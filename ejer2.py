texto=input('ingrese palabra: ')
alfabeto= ('AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz')
contador=0

for i in texto:
    if texto in alfabeto:
        contador+=1

    else:
        print("no todos los carcteres son alfabeticos")
        break
if contador==len(texto):
        print("todos los caracteres son alfabeticos")